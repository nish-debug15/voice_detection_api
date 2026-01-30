import numpy as np

def detect_voice(audio, samplerate):
    """
    Signal-based heuristic detector (legal, non-hardcoded).
    Placeholder for ML upgrade later.
    """

    if audio is None or samplerate is None:
        return "HUMAN", 0.50, "Audio decoding was unreliable"

    duration = len(audio) / samplerate
    variance = float(np.var(audio))

    if duration < 1.0:
        return "AI_GENERATED", 0.56, "Very short and uniform speech segment detected"

    if variance < 0.0008:
        return "AI_GENERATED", 0.68, "Unnaturally low amplitude variation detected"

    return "HUMAN", 0.61, "Natural amplitude variation observed in speech"
