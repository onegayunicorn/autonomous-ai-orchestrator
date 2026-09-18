"""Individual model — Word, Meaning, Feeling, Number, Equation"""
from dataclasses import dataclass
from typing import Optional

@dataclass
class Individual:
    word: str = ""
    meaning: str = ""
    feeling: float = 0.0
    number: float = 0.0
    equation: Optional[str] = None

    def evaluate(self) -> str:
        if abs(self.feeling) < 0.1 and self.number == 0:
            return "neutral"
        if self.feeling > 0.3:
            return "Authentic"
        return "in_progress"
