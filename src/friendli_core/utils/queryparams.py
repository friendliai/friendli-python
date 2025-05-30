"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from typing import (
    Any,
    Dict,
    List,
    Optional,
    get_type_hints,
)

from pydantic import BaseModel
from pydantic.fields import FieldInfo

from .forms import _populate_form
from .metadata import (
    QueryParamMetadata,
    find_field_metadata,
)
from .values import (
    _get_serialized_params,
    _is_set,
    _populate_from_globals,
    _val_to_string,
)


def get_query_params(
    query_params: Any,
    gbls: Optional[Any] = None,
) -> Dict[str, List[str]]:
    params: Dict[str, List[str]] = {}

    globals_already_populated = _populate_query_params(query_params, gbls, params, [])
    if _is_set(gbls):
        _populate_query_params(gbls, None, params, globals_already_populated)

    return params


def _populate_query_params(
    query_params: Any,
    gbls: Any,
    query_param_values: Dict[str, List[str]],
    skip_fields: List[str],
) -> List[str]:
    globals_already_populated: List[str] = []

    if not isinstance(query_params, BaseModel):
        return globals_already_populated

    param_fields: Dict[str, FieldInfo] = query_params.__class__.model_fields
    param_field_types = get_type_hints(query_params.__class__)
    for name in param_fields:
        if name in skip_fields:
            continue

        field = param_fields[name]

        metadata = find_field_metadata(field, QueryParamMetadata)
        if not metadata:
            continue

        value = getattr(query_params, name) if _is_set(query_params) else None

        value, global_found = _populate_from_globals(
            name, value, QueryParamMetadata, gbls
        )
        if global_found:
            globals_already_populated.append(name)

        f_name = field.alias if field.alias is not None else name
        serialization = metadata.serialization
        if serialization is not None:
            serialized_parms = _get_serialized_params(
                metadata, f_name, value, param_field_types[name]
            )
            for key, value in serialized_parms.items():
                if key in query_param_values:
                    query_param_values[key].extend(value)
                else:
                    query_param_values[key] = [value]
        else:
            style = metadata.style
            if style == "deepObject":
                _populate_deep_object_query_params(f_name, value, query_param_values)
            elif style == "form":
                _populate_delimited_query_params(
                    metadata, f_name, value, ",", query_param_values
                )
            elif style == "pipeDelimited":
                _populate_delimited_query_params(
                    metadata, f_name, value, "|", query_param_values
                )
            else:
                raise NotImplementedError(
                    f"query param style {style} not yet supported"
                )

    return globals_already_populated


def _populate_deep_object_query_params(
    field_name: str,
    obj: Any,
    params: Dict[str, List[str]],
):
    if not _is_set(obj):
        return

    if isinstance(obj, BaseModel):
        _populate_deep_object_query_params_basemodel(field_name, obj, params)
    elif isinstance(obj, Dict):
        _populate_deep_object_query_params_dict(field_name, obj, params)


def _populate_deep_object_query_params_basemodel(
    prior_params_key: str,
    obj: Any,
    params: Dict[str, List[str]],
):
    if not _is_set(obj) or not isinstance(obj, BaseModel):
        return

    obj_fields: Dict[str, FieldInfo] = obj.__class__.model_fields
    for name in obj_fields:
        obj_field = obj_fields[name]

        f_name = obj_field.alias if obj_field.alias is not None else name

        params_key = f"{prior_params_key}[{f_name}]"

        obj_param_metadata = find_field_metadata(obj_field, QueryParamMetadata)
        if not _is_set(obj_param_metadata):
            continue

        obj_val = getattr(obj, name)
        if not _is_set(obj_val):
            continue

        if isinstance(obj_val, BaseModel):
            _populate_deep_object_query_params_basemodel(params_key, obj_val, params)
        elif isinstance(obj_val, Dict):
            _populate_deep_object_query_params_dict(params_key, obj_val, params)
        elif isinstance(obj_val, List):
            _populate_deep_object_query_params_list(params_key, obj_val, params)
        else:
            params[params_key] = [_val_to_string(obj_val)]


def _populate_deep_object_query_params_dict(
    prior_params_key: str,
    value: Dict,
    params: Dict[str, List[str]],
):
    if not _is_set(value):
        return

    for key, val in value.items():
        if not _is_set(val):
            continue

        params_key = f"{prior_params_key}[{key}]"

        if isinstance(val, BaseModel):
            _populate_deep_object_query_params_basemodel(params_key, val, params)
        elif isinstance(val, Dict):
            _populate_deep_object_query_params_dict(params_key, val, params)
        elif isinstance(val, List):
            _populate_deep_object_query_params_list(params_key, val, params)
        else:
            params[params_key] = [_val_to_string(val)]


def _populate_deep_object_query_params_list(
    params_key: str,
    value: List,
    params: Dict[str, List[str]],
):
    if not _is_set(value):
        return

    for val in value:
        if not _is_set(val):
            continue

        if params.get(params_key) is None:
            params[params_key] = []

        params[params_key].append(_val_to_string(val))


def _populate_delimited_query_params(
    metadata: QueryParamMetadata,
    field_name: str,
    obj: Any,
    delimiter: str,
    query_param_values: Dict[str, List[str]],
):
    _populate_form(
        field_name,
        metadata.explode,
        obj,
        delimiter,
        query_param_values,
    )
