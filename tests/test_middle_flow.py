import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from src.core.middle_flow import MiddleFlowEngine

def test_equilibrium_damping():
    engine = MiddleFlowEngine(center=0.0, sensitivity=0.1)
    pos = engine.step(push=1.0, pull=0.0)
    assert pos > 0.0
    engine2 = MiddleFlowEngine(center=0.0, sensitivity=0.1)
    pos2 = engine2.step(push=0.0, pull=1.0)
    assert pos2 < 0.0

def test_stability_threshold():
    engine = MiddleFlowEngine(center=0.0, sensitivity=1.0, clamp=5.0)
    for _ in range(100):
        engine.step(push=1.0, pull=0.0)
    assert abs(engine.position) <= 5.0
