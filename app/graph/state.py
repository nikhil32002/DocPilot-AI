from typing import TypedDict
from app.models.task import Task


class AgentState(TypedDict):
    request: str

    document_title: str
    document_type: str

    assumptions: list[str]
    sections: list[str]

    execution_plan: list[Task]

    generated_sections: dict[str, str]

    quality_score: int
    reflection_status: str
    reflection_feedback: str

    retry_count: int

    output_file: str