from fastapi import FastAPI, Depends, HTTPException
from app.schemas import VoiceDetectionRequest, VoiceDetectionResponse
from app.auth import verify_api_key
from app.audio_utils import decode_base64_mp3
from app.detector import detect_voice
from app.config import SUPPORTED_LANGUAGES

app = FastAPI(title="AI Generated Voice Detection API")

@app.post(
    "/api/voice-detection",
    response_model=VoiceDetectionResponse
)
def voice_detection(
    request: VoiceDetectionRequest,
    api_key: str = Depends(verify_api_key)
):
    # Validate language
    if request.language not in SUPPORTED_LANGUAGES:
        raise HTTPException(status_code=400, detail="Unsupported language")

    # Validate format
    if request.audioFormat.lower() != "mp3":
        raise HTTPException(status_code=400, detail="Only mp3 format supported")

    # Decode audio
    audio, samplerate = decode_base64_mp3(request.audioBase64)

    # Detect
    classification, confidence, explanation = detect_voice(audio, samplerate)

    # Response
    return {
        "status": "success",
        "language": request.language,
        "classification": classification,
        "confidenceScore": round(confidence, 2),
        "explanation": explanation
    }
