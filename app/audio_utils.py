import base64
import io
import soundfile as sf

def decode_base64_mp3(audio_base64: str):
    try:
        audio_bytes = base64.b64decode(audio_base64)
        audio_buffer = io.BytesIO(audio_bytes)
        audio, samplerate = sf.read(audio_buffer)
        return audio, samplerate
    except Exception:
        return None, None
