import re
from datetime import date, datetime
from pathlib import Path

import aisuite as ai

from agents import *


class PerAgentTraceSink:
    def __init__(self, directory: Path) -> None:
        self.directory = directory
        self.timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S-%f")
        self.stores: dict[str, ai.tracing.JsonlTraceStore] = {}

    def emit(self, event: ai.tracing.TraceEvent) -> None:
        store = self.stores.get(event.agent_name)
        if store is None:
            safe_agent_name = re.sub(r"[^A-Za-z0-9_-]+", "_", event.agent_name).strip("_")
            path = self.directory / f"{self.timestamp}_{safe_agent_name}.jsonl"
            store = ai.tracing.JsonlTraceStore(path)
            self.stores[event.agent_name] = store
        store.append_event(event)


def main() -> None:
    client = ai.Client(
        provider_configs={
            "ollama": {
                "base_url": "http://127.0.0.1:11434",
                "timeout": 360,
            }
        }
    )

    _, delegate_research = build_researcher()
    _, delegate_investigator = build_investigator()
    _, delegate_editor = build_editor()
    _, delegator_outliner = build_outliner()

    manager = ai.Agent(
        name="Research Manager",
        model="ollama:qwen3:8b",
        instructions=(
            f"""
            You are the Research Manager. Understand the user's request, 
            break down research questions into focused tasks, and delegate 
            research topics to your specialists.
            You have access to:
            - an research investigator that will search the internet for facts and citations using delegate_investigator
            - a research report writer that can look up additional facts by using internet searches using delegate_research
            - an editor that specializes in reviewing reports using delegate_editor
            - a research report outliner that will create the outline of a research report distilling a list of facts down to an actionable list using delegate_editor
            For research questions, delegate to least two distinct agents before answering. 
            Review the specialist's evidence, synthesize a clear answer, cite the supplied source 
            URLs, and call out important limitations or uncertainty. Do not 
            claim to have verified anything that is not in the research 
            report. If the investigator reports arXiv as unavailable, say so
            explicitly and do not describe that as a search with no results.
            The current date is {date.today().strftime('%Y-%m-%d')}.
            Return a well polished, clear report that is easy to digest with no additional commentary.  
            The report must be written in markdown.  
            All citations must be gathered at the end of the report.
            """
        ),
        tools=[delegate_research, delegate_investigator, delegate_editor, delegator_outliner],
    )

    question = input("Ask the Research Manager: ").strip()
    if question:
        trace_sink = PerAgentTraceSink(
            Path(__file__).resolve().parent.parent / "traces"
        )
        result = ai.Runner.run_sync(
            manager,
            question,
            client=client,
            max_turns=20,
            trace_sinks=[trace_sink],
        )
        print(result.final_output)
        fileNamer, _ = build_fileNamer()
        name = ai.Runner.run_sync(
            fileNamer,
            question,
            client=client,
            max_turns=2
        )
        
        with open(f"./reports/{name.final_output}", "w", encoding="utf-8") as file:
            file.write(result.final_output)


if __name__ == "__main__":
    main()
