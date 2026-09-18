import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from src.core.volition import VolitionEngine

def test_volition_matrix():
    engine = VolitionEngine()
    assert engine.process(True, True)[0] == "will"
    assert engine.process(True, False)[0] == "dont"
    assert engine.process(False, True)[0] == "dont"
    assert engine.process(False, False)[0] == "bloat"

def test_bloat_dissolution():
    engine = VolitionEngine()
    result = engine.dissolve_bloat(False, False)
    assert "choose YES OR NO" in result
