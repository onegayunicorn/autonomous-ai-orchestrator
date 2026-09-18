import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from src.core.coherence import CoherenceEngine

def test_coherence_multiplier():
    engine = CoherenceEngine(1, 2)
    assert engine.difference() == 1
    assert engine.sum() == 3
    assert engine.coherence() == 3

def test_coherence_zero():
    engine = CoherenceEngine(5, 5)
    assert engine.difference() == 0
    assert engine.coherence() == 0
