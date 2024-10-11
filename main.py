import os

import inspect_ai

from task.humaneval import humaneval

os.environ["OPENAI_API_KEY"] = "dummy"

inspect_ai.eval(
    tasks=humaneval(),
    model="openai/gpt-4o-mini",
)
