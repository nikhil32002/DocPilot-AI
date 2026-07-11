from pydantic import BaseModel, Field

from app.models.task import Task


class PlannerOutput(BaseModel):

    document_title: str = Field(
        description="Professional document title"
    )

    document_type: str = Field(
        description="Business document type"
    )

    assumptions: list[str] = Field(
        description="Planner assumptions"
    )

    sections: list[str] = Field(
        description="Document sections"
    )

    execution_plan: list[Task] = Field(
        description="Ordered execution tasks"
    )