"""Minimal REST-style API surface (for Vercel / local)"""
from typing import Dict, Any
from src.core.genesis import GenesisEngine
from src.core.middle_flow import MiddleFlowEngine
from src.core.volition import VolitionEngine
from src.core.coherence import CoherenceEngine
from src.core.pulse import SovereignPulseEngine
from src.models.validator import PathValidator

_genesis = GenesisEngine()
_flow = MiddleFlowEngine()
_volition = VolitionEngine()
_coherence = CoherenceEngine()
_pulse = SovereignPulseEngine()
_validator = PathValidator()

def handle(request: Dict[str, Any]) -> Dict[str, Any]:
    action = request.get("action", "status")
    if action == "genesis":
        n = int(request.get("n", 8))
        return {"sequence": _genesis.generate(n), "codex": _genesis.codex_transform()}
    if action == "flow":
        pos = _flow.step(float(request.get("push", 0)), float(request.get("pull", 0)))
        return {"position": pos}
    if action == "volition":
        state, msg = _volition.process(bool(request.get("want")), bool(request.get("will")))
        return {"state": state, "message": msg}
    if action == "coherence":
        c = _coherence.reveal(float(request.get("a", 0)), float(request.get("b", 0)))
        return {"coherence": c}
    if action == "pulse":
        _pulse.pulse()
        return _pulse.unlock_behind()
    if action == "validate":
        return {"message": _validator.get_help_message(request.get("path", ""))}
    return {"status": "ok", "version": "2.6"}
