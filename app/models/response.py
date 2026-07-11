from pydantic import BaseModel

class AgentResponse(BaseModel):
    """
    API response returned to the client.
    """

    status: str

    document_title: str

    document_type: str

    quality_score: int

    output_file: str

    execution_plan: list[str]

    execution_trace: list[str]