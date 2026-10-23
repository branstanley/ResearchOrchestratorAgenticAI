# ResearchOrchestratorAgenticAI
A Orchestrator-Worker pattern Agentic AI for creating a research paper using aisuite.

The project uses a local LLM (Qwen3:8B) for report generation, but could easily switch to use other models thanks to using aisuite.

## To run

Get the LLM agent up and running:
```
docker compose up --build
```

Then to run the code:
```
cd ./agents
pip install -r requirements.txt
python ./program.py
```

Optionally you can use a .venv

## Example report

[Lightbulb Theory and Calculations](<reports/Lightbulb Theory and Calculations.md>)
