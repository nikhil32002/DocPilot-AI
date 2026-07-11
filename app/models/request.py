from pydantic import BaseModel, Field

class AgentRequest(BaseModel):
    """
    Incoming API request from the client.
    """

    request: str = Field(
        ...,
        min_length=10,
        description="Natural language request for the autonomous agent."
    )