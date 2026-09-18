"""Volition Engine — Want/Will matrix & Bloat dissolution"""
from typing import Tuple

class VolitionEngine:
    def process(self, want: bool, will: bool) -> Tuple[str, str]:
        if want and will:
            return "will", "Aligned want and will — move"
        if want and not will:
            return "dont", "My want without your will — release"
        if not want and will:
            return "dont", "Will without want — observe"
        return "bloat", "Neither want nor will — choose YES or NO"

    def dissolve_bloat(self, want: bool, will: bool) -> str:
        state, msg = self.process(want, will)
        if state == "bloat":
            return "Bloat detected. choose YES OR NO — any decision dissolves the hold."
        return msg
