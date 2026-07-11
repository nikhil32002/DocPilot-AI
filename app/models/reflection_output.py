from pydantic import BaseModel, Field


class ReflectionOutput(BaseModel):
    """
    Structured output returned by the Reflection Agent.
    """

    quality_score: int = Field(
        ge=0,
        le=100,
        description="Overall quality score."
    )

    missing_sections: list[str] = Field(
        default_factory=list,
        description="Missing or incomplete document sections."
    )

    feedback: str = Field(
        description="Suggestions for improving the document."
    )