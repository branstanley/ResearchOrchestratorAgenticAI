from collections.abc import Callable
from typing import Any

import aisuite as ai
from aisuite import agent_tool



def build_fileNamer() -> tuple[ai.Agent, Callable[..., Any]]:
    agent = ai.Agent(
        name="FileNamer",
        model="ollama:qwen3:8b",
        instructions=(
            """
            You are an agent that takes a research question, and distills it into a useful file name.
            Your goal is to preserve the concept of the question, but make a USEFUL file name that a user can easily recognize without being more than 5 words
            Output: Only the name of the file, in the format: some_file_name.md
            """
        ),
        tools=[],
    )
    delegate = None
    return agent, delegate
