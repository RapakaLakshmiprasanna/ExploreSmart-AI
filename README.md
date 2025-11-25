# ExploreSmart (Mock Python ADK Repo)

ExploreSmart is a mock, nearly-functional starter repository for a multi-agent travel discovery system (Concierge Agents track).
This repo provides a realistic skeleton (Orchestrator + Search + Preference + Planner + Memory agents) implemented in Python.

## What this is
- Mocked tools (Google Search, Maps) so you can run offline.
- File-based memory store `.mock_memory/`.
- Clear extension points for real ADK integration (ADK-Python, OpenAPI tools).

## How to run (local)
1. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # or .venv\\Scripts\\activate on Windows
   pip install -r requirements.txt
