"""Sovereign Framework v2.6 — Core Loop"""
import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.core.genesis import GenesisEngine
from src.core.middle_flow import MiddleFlowEngine
from src.core.volition import VolitionEngine
from src.core.coherence import CoherenceEngine
from src.core.pulse import SovereignPulseEngine
from src.models.validator import PathValidator

def simulate():
    print("[SYSTEM] Booting Sovereign Framework v2.6...")
    print("[SYSTEM] Loading Genesis Engine... OK")
    print("[SYSTEM] Loading Middle Flow Engine... OK")
    print("[SYSTEM] Loading Volition Engine... OK")
    print("[SYSTEM] Loading Coherence Engine... OK")
    print("[SYSTEM] Loading Validator... OK")
    print("[SYSTEM] Mode: DUAL ACTIVE (Third Eye + Beholder)")

    genesis = GenesisEngine()
    flow = MiddleFlowEngine()
    volition = VolitionEngine()
    coherence = CoherenceEngine()
    pulse = SovereignPulseEngine()
    validator = PathValidator()

    ledger = []
    seq = genesis.generate(8)
    codex = genesis.codex_transform(seq)
    print(f"Genesis: {seq}")
    print(f"Codex:   {codex}")
    ledger.append({"event": "genesis", "n": 8, "coherence_delta": 1.08})

    pos = flow.step(0.8, 0.2)
    print(f"Middle Flow equilibrium: {pos:.4f}")
    ledger.append({"event": "middle_flow", "push": 0.8, "pull": 0.2, "position": pos})

    state, msg = volition.process(True, False)
    print(f"Volition: {state} — {msg}")
    ledger.append({"event": "volition", "state": state})

    c = coherence.reveal(1, 2)
    print(f"Coherence: {c}")
    ledger.append({"event": "coherence", "value": c})

    help_msg = validator.get_help_message("/wrong_turn")
    print(help_msg)
    ledger.append({"event": "validator", "path": "/wrong_turn"})

    for _ in range(3):
        pulse.pulse()
    print(pulse.unlock_behind())

    print("\n[SYSTEM] Terminal State Reached: AUTHENTIC.")
    print(json.dumps({"ledger": ledger, "timestamp": datetime.now(timezone.utc).isoformat()}, indent=2))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", default="simulate", choices=["simulate", "cli"])
    args = parser.parse_args()
    if args.mode == "cli":
        from src.interfaces.cli import run_cli
        run_cli()
    else:
        simulate()
