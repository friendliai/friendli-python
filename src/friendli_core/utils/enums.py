"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

import enum
import sys


class OpenEnumMeta(enum.EnumMeta):
    # The __call__ method `boundary` kwarg was added in 3.11 and must be present
    # for pyright. Refer also: https://github.com/pylint-dev/pylint/issues/9622
    # pylint: disable=unexpected-keyword-arg
    # The __call__ method `values` varg must be named for pyright.
    # pylint: disable=keyword-arg-before-vararg

    if sys.version_info >= (3, 11):

        def __call__(
            cls,
            value,
            names=None,
            *values,
            module=None,
            qualname=None,
            type=None,
            start=1,
            boundary=None,
        ):
            # The `type` kwarg also happens to be a built-in that pylint flags as
            # redeclared. Safe to ignore this lint rule with this scope.
            # pylint: disable=redefined-builtin

            if names is not None:
                return super().__call__(
                    value,
                    names=names,
                    *values,
                    module=module,
                    qualname=qualname,
                    type=type,
                    start=start,
                    boundary=boundary,
                )

            try:
                return super().__call__(
                    value,
                    names=names,  # pyright: ignore[reportArgumentType]
                    *values,
                    module=module,
                    qualname=qualname,
                    type=type,
                    start=start,
                    boundary=boundary,
                )
            except ValueError:
                return value
    else:

        def __call__(
            cls, value, names=None, *, module=None, qualname=None, type=None, start=1
        ):
            # The `type` kwarg also happens to be a built-in that pylint flags as
            # redeclared. Safe to ignore this lint rule with this scope.
            # pylint: disable=redefined-builtin

            if names is not None:
                return super().__call__(
                    value,
                    names=names,
                    module=module,
                    qualname=qualname,
                    type=type,
                    start=start,
                )

            try:
                return super().__call__(
                    value,
                    names=names,  # pyright: ignore[reportArgumentType]
                    module=module,
                    qualname=qualname,
                    type=type,
                    start=start,
                )
            except ValueError:
                return value
