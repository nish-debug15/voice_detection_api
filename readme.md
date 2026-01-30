# AI-Generated Voice Detection API

A production-ready REST API that detects whether a given voice sample is **AI-generated** or **Human**.  
This project is built for the **AI-Generated Voice Detection (Multi-Language)** hackathon problem.

---

## 🚀 Live API (Public)

Base URL  
https://voice-detection-api-uq21.onrender.com

Voice Detection Endpoint  
POST https://voice-detection-api-uq21.onrender.com/api/voice-detection

Swagger UI (Testing & Debugging)  
https://voice-detection-api-uq21.onrender.com/docs

Health Check  
https://voice-detection-api-uq21.onrender.com/health

---

## 🌍 Supported Languages

- Tamil  
- English  
- Hindi  
- Malayalam  
- Telugu  

The language is explicitly provided in the request. Auto-detection is not used.

---

## 🔐 Authentication

All API requests must include an API key.

Header:
x-api-key: sk_test_123456789

Requests without a valid API key are rejected.

---

## 📥 API Request Specification

Endpoint  
POST /api/voice-detection

Headers  
Content-Type: application/json  
x-api-key: sk_test_123456789

Request Body Example:
```json
{
  "language": "Tamil",
  "audioFormat": "mp3",
  "audioBase64": "<BASE64_ENCODED_MP3>"
}
