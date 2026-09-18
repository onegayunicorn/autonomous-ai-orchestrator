import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from src.core.genesis import GenesisEngine

def test_genesis_sequence():
    engine = GenesisEngine(seed=[0, 1])
    assert engine.generate(n=6) == [0, 1, 1, 2, 3, 5]
    assert engine.codex_transform([0, 1, 1, 2, 3, 5]) == [0, 2, 2, 4, 6, 10]

def test_genesis_lightness():
    engine = GenesisEngine()
    assert len(engine.generate(n=10)) == 10
