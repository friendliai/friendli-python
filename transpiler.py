# Copyright (c) 2025-present, FriendliAI Inc. All rights reserved.

"""Transpiler passes."""

from __future__ import annotations

import ast
from collections import defaultdict
from itertools import chain
from typing import Iterator

import sdk_transpiler as st


@st.file_pass(name="basesdk.py")
def update_basesdk_py(ctx: st.FilePassContext) -> None:
    """Run a pass for basesdk.py."""
    ctx.file.add_import("abc")

    def _split_class(klass: st.Class) -> Iterator[st.Class]:
        transformer = st.ClassTransformer(klass)
        base_tf, sync_tf, async_tf = split_sync_async_methods(
            transformer, remove_trailing_async=False
        )

        yield base_tf.add_base_class("abc.ABC").build()
        yield sync_tf.clear_annotation().build()
        yield async_tf.clear_annotation().build()

    for klass in ctx.iter_classes(name="BaseSDK"):
        klass.modify(_split_class)


SdkModuleNamespaceToClassNames: defaultdict[str, list[str]] = defaultdict(list)


@st.file_pass(name_not_in=["basesdk.py", "sdk.py"])
def register_sdk_components(ctx: st.FilePassContext) -> None:
    """Run a pass to register SDK components."""
    if not (sdks := list(ctx.iter_classes(base_contains="BaseSDK"))):
        return

    ctx.add_import("abc")
    import_ = ctx.get_import(module_has="basesdk")
    import_.modify(_update_basesdk_import)

    for klass in sdks:
        SdkModuleNamespaceToClassNames[ctx.module or ""].append(klass.name)


@st.file_pass(name_not_in=["basesdk.py", "sdk.py"])
def split_sdk_components(ctx: st.FilePassContext) -> None:
    """Run a pass to modify SDK classes."""

    def _split_class(klass: st.Class) -> Iterator[st.Class]:
        init_sdk_method = klass.get_method(name="_init_sdks")
        tf = st.ClassTransformer(klass)
        base_tf, sync_tf, async_tf = split_sync_async_methods(tf)

        if init_sdk_method:
            sync_tf = sync_tf.add_method(init_sdk_method)
            async_tf = async_tf.add_method(init_sdk_method)
            base_tf = base_tf.remove_method("_init_sdks").add_method(
                ast.parse("def _init_sdks(self) -> None: ...").body[0]
            )

        yield (base_tf.clear_annotation().build())

        sync_tf = sync_tf.remove_base_class("BaseSDK").add_base_class("SyncSDK")
        async_tf = async_tf.remove_base_class("BaseSDK").add_base_class("AsyncSDK")

        yield _handle_class(sync_tf, "Sync", SdkModuleNamespaceToClassNames)
        yield _handle_class(async_tf, "Async", SdkModuleNamespaceToClassNames)

    if not (sdks := list(ctx.iter_classes(base_contains="BaseSDK"))):
        return

    for klass in sdks:
        klass.modify(_split_class)


@st.file_pass(name="sdk.py")
def split_sdk_py(ctx: st.FilePassContext) -> None:
    """Run a pass to modify SDK classes."""

    def _split_class(klass: st.Class) -> Iterator[st.Class]:
        tf = st.ClassTransformer(klass)
        base_tf, sync_tf, async_tf = split_sync_async_methods(tf)

        yield (
            base_tf.clear_annotation()
            .clear_attribute()
            .add_annotation("_sub_sdk_map", "dict[str, tuple[str, str]]")
            .build()
        )

        sync_tf = sync_tf.remove_base_class("BaseSDK").add_base_class("SyncSDK")
        async_tf = async_tf.remove_base_class("BaseSDK").add_base_class("AsyncSDK")

        yield _handle_class(sync_tf, "Sync", SdkModuleNamespaceToClassNames)
        yield _handle_class(async_tf, "Async", SdkModuleNamespaceToClassNames)

    if not (sdks := list(ctx.iter_classes(base_contains="BaseSDK"))):
        return

    ctx.add_import("abc")
    import_ = ctx.get_import(module_has="basesdk")
    import_.modify(_update_basesdk_import)

    for klass in sdks:
        klass.modify(_split_class)


@st.file_pass
def modify_sdk_import_statement_pass(ctx: st.FilePassContext) -> None:
    """Run a pass to modify import statement."""

    def _update_sdk_import(import_: st.Import) -> Iterator[st.Import]:
        tf = st.ImportTransformer(import_)

        for name in SdkModuleNamespaceToClassNames[import_.module or ""]:
            tf = tf.remove_name(name).add_names(f"Sync{name}", f"Async{name}")

        yield tf.build()

    for import_ in ctx.iter_imports(module_in=SdkModuleNamespaceToClassNames):
        import_.modify(_update_sdk_import)


@st.file_pass
def modify_import_statement_pass(ctx: st.FilePassContext) -> None:
    """Run a pass to modify import statement."""

    def _update_import(import_: st.Import) -> Iterator[st.Import]:
        yield (
            st.ImportTransformer(import_)
            .replace_module("friendli_core", to="friendli.core")
            .build()
        )

    for import_ in ctx.iter_imports():
        import_.modify(_update_import)


def split_sync_async_methods(
    st: st.ClassTransformer, *, remove_trailing_async: bool = True
) -> tuple[st.ClassTransformer, st.ClassTransformer, st.ClassTransformer]:
    """Split a class into base/sync/async classes.

    Finds all async methods and corresponding sync methods to split methods into
    appropriate classes.

    Args:
        st: ClassTransformer
        remove_trailing_async: Whether to remove _async suffix from async methods.

    """
    cls_name = st.klass.name.removeprefix("Base")
    async_methods = list(st.klass.iter_methods(async_method=True))
    sync_method_names = [_async_to_sync_name(m.name) for m in async_methods]
    sync_methods = list(st.klass.iter_methods(names_in=sync_method_names))

    base_tf = (
        st.update_name(f"Base{cls_name}")
        .remove_method(*async_methods)
        .remove_method(*sync_methods)
    )

    ctf = st.add_base_class(f"Base{cls_name}")
    sync_tf = ctf.update_name(f"Sync{cls_name}").remove_method_but(*sync_methods)
    async_tf = ctf.update_name(f"Async{cls_name}").remove_method_but(*async_methods)
    if remove_trailing_async:
        for method in async_methods:
            async_tf = async_tf.rename_method(
                method.name, method.name.removesuffix("_async")
            )

    return base_tf, sync_tf, async_tf


def _async_to_sync_name(name: str) -> str:
    """Convert async method name to sync method name."""
    if name == "__aenter__":
        return "__enter__"
    if name == "__aexit__":
        return "__exit__"
    return name.removesuffix("_async")


def _update_basesdk_import(import_: st.Import) -> Iterator[st.Import]:
    tf = st.ImportTransformer(import_)
    yield tf.add_names("SyncSDK", "AsyncSDK").build()


def _handle_class(
    tf: st.ClassTransformer,
    prefix: str,
    namespace_to_class_names: dict[str, list[str]],
) -> st.Class:
    names = {
        name: f"{prefix}{name}"
        for name in chain.from_iterable(namespace_to_class_names.values())
    }
    names["friendli_core"] = "friendli.core"
    return tf.refactor_names(names).build()
