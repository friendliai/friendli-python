# Copyright (c) 2025-present, FriendliAI Inc. All rights reserved.

"""Friendli Python SDK Models."""

from __future__ import annotations

import base64
import binascii
from typing import (
    TYPE_CHECKING,
    Annotated,
    Any,
    ByteString,
    Callable,
    Literal,
    Union,
    cast,
)

from pydantic import (
    AnyHttpUrl,
    AnyUrl,
    BaseModel,
    Field,
    RootModel,
    UrlConstraints,
    field_validator,
)

from friendli_core.models import *  # noqa: F403

if TYPE_CHECKING:
    from pydantic.config import JsonDict


# NOTE: This originates from `pfapp/backend/openapi/utils.py`.


def fix_oneof_schema(titles: list[str]) -> Callable[[JsonDict], None]:
    """Fix oneOf schema by adding title to each model."""

    def _fixer(schema: JsonDict) -> None:
        discriminator = schema.get("discriminator")
        oneof = schema.get("oneOf")
        if not discriminator or not oneof:
            return

        discriminator = cast("JsonDict", discriminator)

        oneof_with_title = [
            {**model, "title": title}
            for title, model in zip(titles, cast("Any", oneof), strict=True)
        ]
        schema.pop("title")
        schema["oneOf"] = oneof_with_title  # type: ignore

    return _fixer


def fix_union_schema(
    titles: list[str], **extra_json_schema: Any
) -> Callable[[JsonDict], None]:
    """Fix union schema by adding title to each model."""

    def _fixer(schema: JsonDict) -> None:
        oneof = schema.get("oneOf")
        if not oneof:
            return

        oneof_with_title = [
            {**model, "title": title}
            for title, model in zip(titles, cast("Any", oneof), strict=True)
        ]
        schema.pop("title")
        schema["oneOf"] = oneof_with_title  # type: ignore
        schema.update(extra_json_schema)

    return _fixer


# NOTE: This originates from `pfapp/backend/openapi/route/common.py`.


class SystemMessage(BaseModel):
    role: Literal["system"] = Field(..., description="The role of the messages author.")
    content: str = Field(..., description="The content of system message.")
    name: str | None = Field(
        None,
        description="The name for the participant to distinguish between participants with the same role.",
    )


class TextContent(BaseModel):
    type: Literal["text"] = Field(..., description="The type of the message content.")
    text: str = Field(..., description="The text content of the message.")


class AudioData(BaseModel):
    url: str = Field(..., description="The URL of the audio.")


BASE64_IMAGE_PREFIXES = (
    "data:image/png;base64,",
    "data:image/jpeg;base64,",
    "data:image/jpg;base64,",
    "data:image/gif;base64,",
)


class ImageData(BaseModel):
    type: Literal["image"] = Field(..., description="The type of the message content.")
    image: str = Field(..., description="The URL or base64 string of the image.")

    @field_validator("image")
    @classmethod
    def validate_image(cls, v: str) -> str:
        if any(v.startswith(prefix) for prefix in BASE64_IMAGE_PREFIXES):
            try:
                base64_data = v.split(sep=",", maxsplit=1)[1]
                base64.b64decode(base64_data, validate=True)
            except binascii.Error:
                raise ValueError("`image` must be a valid base64 string.")
            return v
        try:
            AnyHttpUrl(v)
        except ValueError:
            try:
                S3Dsn(v)
            except ValueError:
                raise ValueError("`image` must be a valid HTTP URL or S3 URL.")
        return v


class ImageUrl(BaseModel):
    url: str = Field(..., description="The URL of the image.")

    @field_validator("url")
    @classmethod
    def validate_url(cls, v: str) -> str:
        try:
            AnyHttpUrl(v)
        except ValueError:
            try:
                S3Dsn(v)
            except ValueError:
                raise ValueError("`url` must be a valid HTTP URL or S3 URL.")
        return v


class ImageUrlData(BaseModel):
    type: Literal["image_url"] = Field(
        ..., description="The type of the message content."
    )
    image_url: str | ImageUrl = Field(
        ..., description="The URL of the image or image data object."
    )

    def to_ImageData(self) -> ImageData:
        if isinstance(self.image_url, str):
            return ImageData(type="image", image=self.image_url)
        if isinstance(self.image_url, ImageUrl):
            return ImageData(type="image", image=self.image_url.url)


class VideoData(BaseModel):
    url: str = Field(..., description="The URL of the video.")


class AudioContent(BaseModel):
    type: Literal["audio_url"] = Field(
        ..., description="The type of the message content."
    )
    audio_url: AudioData = Field(..., description="The audio URL data.")


class ImageContent(RootModel[ImageData | ImageUrlData]):
    root: ImageData | ImageUrlData = Field(
        discriminator="type",
        json_schema_extra=fix_oneof_schema(["Image", "ImageUrl"]),
    )


class VideoContent(BaseModel):
    type: Literal["video_url"] = Field(
        ..., description="The type of the message content."
    )
    video_url: VideoData = Field(..., description="The video URL data.")


class UserMessageContentMultiModal(
    RootModel[TextContent | AudioContent | ImageContent | VideoContent]
):
    root: TextContent | AudioContent | ImageContent | VideoContent = Field(
        discriminator="type",
        json_schema_extra=fix_oneof_schema(["Text", "Audio", "Image", "Video"]),
    )


UserMessageContentString = Annotated[
    str,
    Field(
        description=(
            "The content of user message, which is plain text.\n\n"
            "For **multi-modal format**, use `object[]` type. Support "
            "for non-text input is currently in **Beta**."
        )
    ),
]

UserMessageContentArray = Annotated[
    list[UserMessageContentMultiModal],
    Field(
        description=(
            "The content of user message.\n\n"
            "**Multi-modal format** can handle not just text, but also audio, "
            "image, and video content, allowing for more complex message structures. "
            "Support for non-text input is currently in **Beta**."
        )
    ),
]


class UserMessage(BaseModel):
    role: Literal["user"] = Field(..., description="The role of the message's author.")
    content: Union[UserMessageContentString, UserMessageContentArray] = Field(
        ..., title="Content"
    )
    name: str | None = Field(
        None,
        description="The name for the participant to distinguish between participants with the same role.",
    )


class AssistantMessageToolCallFunction(BaseModel):
    name: str = Field(..., description="The name of function")
    arguments: str = Field(
        ...,
        description="The arguments of function in JSON schema format to call the function.",
    )


class AssistantMessageToolCall(BaseModel):
    id: str = Field(..., description="The ID of tool call.")
    type: Literal["function"] = Field(..., description="The type of tool call.")
    function: AssistantMessageToolCallFunction = Field(
        ..., description="The function specification"
    )


class AssistantMessage(BaseModel):
    role: Literal["assistant"] = Field(
        ..., description="The role of the messages author."
    )
    content: str | None = Field(
        None,
        description="The content of assistant message. Required unless `tool_calls` is specified.",
    )
    name: str | None = Field(
        None,
        description="The name for the participant to distinguish between participants with the same role.",
    )
    tool_calls: list[AssistantMessageToolCall] | None = None


class ToolMessage(BaseModel):
    role: Literal["tool"] = Field(..., description="The role of the messages author.")
    content: str = Field(
        ...,
        description="The content of tool message that contains the result of tool calling.",
    )
    tool_call_id: str = Field(
        ..., description="The ID of tool call corresponding to this message."
    )
    name: str | None = Field(
        None,
        description="An optional name of the tool call corresponding to this message.",
    )


class Message(RootModel[SystemMessage | UserMessage | AssistantMessage | ToolMessage]):
    root: SystemMessage | UserMessage | AssistantMessage | ToolMessage = Field(
        ...,
        discriminator="role",
        json_schema_extra=fix_oneof_schema(["System", "User", "Assistant", "Tool"]),
    )


class Sample(BaseModel):
    messages: list[Message]


class S3Dsn(AnyUrl):
    """A type that will accept any Amazon S3 URI.

    This is a custom type. Refer to `pydantic.networks.AnyUrl` and its derived types for details.

    Format: s3://<bucket_name>/<path>
    """

    _constraints = UrlConstraints(allowed_schemes=["s3"])
