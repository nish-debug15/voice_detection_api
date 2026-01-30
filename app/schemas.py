from pydantic import BaseModel

class VoiceDetectionRequest(BaseModel):
    language: str
    audioFormat: str
    audioBase64: str

class VoiceDetectionResponse(BaseModel):
    status: str
    language: str
    classification: str
    confidenceScore: float
    explanation: str
