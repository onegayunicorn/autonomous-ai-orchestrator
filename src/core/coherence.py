"""Coherence Engine — Difference × Sum multiplier"""
class CoherenceEngine:
    def __init__(self, val_a: float = 0, val_b: float = 0):
        self.a = val_a
        self.b = val_b

    def difference(self) -> float:
        return abs(self.a - self.b)

    def sum(self) -> float:
        return self.a + self.b

    def coherence(self) -> float:
        d = self.difference()
        if d == 0:
            return 0.0
        return self.sum() * d

    def reveal(self, val_a: float, val_b: float) -> float:
        self.a = val_a
        self.b = val_b
        return self.coherence()
