# Sovereign Framework v2.6

**Status:** Architecture verified · 9 tests green · Local-only  
**Mode:** Third Eye + Beholder (Dual Active)  
**Terminal State:** AUTHENTIC

Modular monolith mapping philosophical contracts to deterministic engines.

## Quick Start

```bash
python -m src.main --mode=simulate
python -m src.main --mode=cli
python -m pytest tests/ -v
```

## Structure

```
config/          engine.yaml · weights.json
src/core/        genesis · middle_flow · volition · coherence · pulse
src/models/      individual · reflection · validator
src/interfaces/  cli · web_api
tests/           full suite including 9-Realms integration
biofeedback/     Schumann + HRV bridge (local-only)
vercel/          deployment package
```

## Core Contracts

| Engine       | Input              | Output                  |
|--------------|--------------------|-------------------------|
| Genesis      | n                  | Fibonacci + Codex       |
| Middle Flow  | push, pull         | damped equilibrium      |
| Volition     | want, will         | will / dont / bloat     |
| Coherence    | a, b               | (a+b)×|a-b|             |
| Validator    | path               | unsaid help / clear     |

## Schumann + HRV

See `biofeedback/schumann_hrv.py`.  
Peer-reviewed correlations between Schumann power / geomagnetic activity and HRV exist; resonance-frequency breathing (~0.1 Hz) is an evidence-based biofeedback protocol. All processing is local-first; reality manipulation remains OFF.

## License

MIT · Sovereign local use
