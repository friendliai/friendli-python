# DedicatedAudioTranscriptionBodyChunkingStrategy

Controls how the audio is cut into chunks. When set to `"auto"`, the server first normalizes loudness and then uses voice activity detection (VAD) to choose boundaries. `server_vad` object can be provided to tweak VAD detection parameters manually. If unset, the audio is transcribed as a single block.


## Supported Types

### `str`

```python
value: str = /* values here */
```

### `models.ServerVadChunkingStrategy`

```python
value: models.ServerVadChunkingStrategy = /* values here */
```

