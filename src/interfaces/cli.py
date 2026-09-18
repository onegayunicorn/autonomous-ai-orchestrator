"""CLI interface for Sovereign Framework"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from src.core.genesis import GenesisEngine
from src.core.middle_flow import MiddleFlowEngine
from src.core.volition import VolitionEngine
from src.core.coherence import CoherenceEngine
from src.core.pulse import SovereignPulseEngine
from src.models.validator import PathValidator

def run_cli():
    print("Sovereign Framework v2.6 — CLI")
    print("Commands: genesis <n> | flow <push> <pull> | volition <want> <will> | coherence <a> <b> | pulse | help <path> | quit")
    genesis = GenesisEngine()
    flow = MiddleFlowEngine()
    volition = VolitionEngine()
    coherence = CoherenceEngine()
    pulse = SovereignPulseEngine()
    validator = PathValidator()

    while True:
        try:
            line = input("> ").strip()
        except EOFError:
            break
        if not line or line == "quit":
            break
        parts = line.split()
        cmd = parts[0].lower()
        if cmd == "genesis" and len(parts) > 1:
            print(genesis.generate(int(parts[1])))
        elif cmd == "flow" and len(parts) > 2:
            print(flow.step(float(parts[1]), float(parts[2])))
        elif cmd == "volition" and len(parts) > 2:
            want = parts[1].lower() in ("1", "true", "yes")
            will = parts[2].lower() in ("1", "true", "yes")
            print(volition.process(want, will))
        elif cmd == "coherence" and len(parts) > 2:
            print(coherence.reveal(float(parts[1]), float(parts[2])))
        elif cmd == "pulse":
            pulse.pulse()
            print(pulse.unlock_behind())
        elif cmd == "help" and len(parts) > 1:
            print(validator.get_help_message(parts[1]))
        else:
            print("Unknown or incomplete command")
