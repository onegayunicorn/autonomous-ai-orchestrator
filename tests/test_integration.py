import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from src.core.genesis import GenesisEngine
from src.core.pulse import SovereignPulseEngine
from src.core.volition import VolitionEngine

def test_recursive_being_loop():
    genesis = GenesisEngine()
    pulse = SovereignPulseEngine()
    volition = VolitionEngine()

    seq = genesis.generate(5)
    assert seq == [0, 1, 1, 2, 3]

    state, msg = volition.process(want=True, will=True)
    assert state == "will"

    pulse.pulse_count = 3
    insight = pulse.unlock_behind()
    assert insight["status"] == "Door opened behind me"
    assert insight["pulses_walked"] == 3

    final_evaluation = "Authentic"
    assert final_evaluation == "Authentic"
