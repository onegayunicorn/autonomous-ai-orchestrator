"""Sovereign Pulse / Retroaction Engine"""
from typing import Dict, Any

class SovereignPulseEngine:
    def __init__(self):
        self.pulse_count = 0
        self.history = []

    def pulse(self) -> int:
        self.pulse_count += 1
        self.history.append(self.pulse_count)
        return self.pulse_count

    def unlock_behind(self) -> Dict[str, Any]:
        return {
            "status": "Door opened behind me",
            "pulses_walked": self.pulse_count,
            "insight": "The path already walked contains the feedback you need."
        }
