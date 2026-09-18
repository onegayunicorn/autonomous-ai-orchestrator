"""
Schumann Resonance + HRV Biofeedback Integration
Local-only, device-bound. Reality manipulation remains OFF.
"""
import math
from typing import Dict, Optional

SCHUMANN = 7.83
PHI = (1 + math.sqrt(5)) / 2
TARGET_RESONANCE_HZ = 0.1  # ~6 breaths/min classic HRV biofeedback

class SchumannHRVBridge:
    """
    Maps Schumann carrier + optional HRV metrics into a coherence contribution.
    Peer-reviewed context:
    - HRV synchronizes with geomagnetic / Schumann power (PMC5551208, Nature SciRep 2018).
    - Resonance-frequency breathing (~0.1 Hz) amplifies HRV and baroreflex gain (Lehrer et al.).
    - Correlations exist; strong single-person causal claims remain modest.
    """

    def __init__(self):
        self.phase = 0.0

    def schumann_phase(self, t: float) -> float:
        return (2 * math.pi * SCHUMANN * t) % (2 * math.pi)

    def resonance_breath_target(self) -> float:
        return TARGET_RESONANCE_HZ

    def coherence_contribution(
        self,
        hrv_rmssd: Optional[float] = None,
        breathing_rate_hz: Optional[float] = None,
        t: float = 0.0,
    ) -> Dict:
        base = 0.01 * math.sin(self.schumann_phase(t))
        if breathing_rate_hz is not None:
            proximity = max(0.0, 1.0 - abs(breathing_rate_hz - TARGET_RESONANCE_HZ) * 10)
            base += 0.02 * proximity
        if hrv_rmssd is not None and hrv_rmssd > 20:
            base += min(0.02, (hrv_rmssd - 20) / 2000)
        return {
            "contribution": round(max(0.0, min(0.05, base)), 5),
            "schumann_hz": SCHUMANN,
            "target_breath_hz": TARGET_RESONANCE_HZ,
            "note": "local report only — no actuation",
        }
