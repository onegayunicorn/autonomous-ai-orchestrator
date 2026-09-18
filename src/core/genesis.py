"""Genesis Engine — Fibonacci recursion & amplification"""
from typing import List

class GenesisEngine:
    def __init__(self, seed: List[int] = None):
        self.seed = seed or [0, 1]

    def generate(self, n: int) -> List[int]:
        if n <= 0:
            return []
        seq = list(self.seed)
        while len(seq) < n:
            seq.append(seq[-1] + seq[-2])
        return seq[:n]

    def codex_transform(self, seq: List[int] = None) -> List[int]:
        if seq is None:
            seq = self.generate(8)
        return [x * 2 for x in seq]
