# MessagesBase64ImageSource


## Fields

| Field                                                 | Type                                                  | Required                                              | Description                                           |
| ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- |
| `type`                                                | *Literal["base64"]*                                   | :heavy_check_mark:                                    | Image source type. Must be `base64`.                  |
| `data`                                                | *str*                                                 | :heavy_check_mark:                                    | Base64-encoded image bytes (without data URL prefix). |
| `media_type`                                          | *str*                                                 | :heavy_check_mark:                                    | MIME type, for example `image/png`.                   |