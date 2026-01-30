from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel

app = FastAPI(
    title="AI Generated Voice Detection API",
    docs_url="/docs",
    redoc_url="/redoc"
)

API_KEY = "sk_test_123456789"

SUPPORTED_LANGUAGES = {
    "tamil": "Tamil",
    "english": "English",
    "hindi": "Hindi",
    "malayalam": "Malayalam",
    "telugu": "Telugu"
}

class VoiceRequest(BaseModel):
    language: str
    audioFormat: str
    audioBase64: str


@app.get("/")
def root():
    return {
        "status": "running",
        "message": "Voice Detection API is live"
    }


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/api/voice-detection")
def voice_detection_get():
    return {
        "status": "error",
        "message": "Use POST method for voice detection"
    }


@app.post("/api/voice-detection")
def voice_detection(
    data: VoiceRequest,
    x_api_key: str = Header(None)
):
    if x_api_key != API_KEY:
        raise HTTPException(
            status_code=401,
            detail="Invalid API key or malformed request"
        )

    language_key = data.language.strip().lower()
    audio_format = data.audioFormat.strip().lower()

    if language_key not in SUPPORTED_LANGUAGES:
        raise HTTPException(
            status_code=400,
            detail=f"Unsupported language: {data.language}"
        )

    if audio_format != "mp3":
        raise HTTPException(
            status_code=400,
            detail="Only mp3 audio format is supported"
        )

    if not data.audioBase64 or len(data.audioBase64) < 100:
        raise HTTPException(
            status_code=400,
            detail="Invalid or empty audioBase64 input"
        )

    return {
        "status": "success",
        "language": SUPPORTED_LANGUAGES[language_key],
        "classification": "HUMAN",
        "confidenceScore": 0.55,
        "explanation": "Baseline response for endpoint validation"
    }
