from fastapi import APIRouter

from app.graph.workflow import graph
from app.models.request import AgentRequest

router = APIRouter()


@router.post("/agent")
def run_agent(request: AgentRequest):

    initial_state = {
        "request": request.request,
        "generated_sections": {},
        "retry_count": 0
    }

    result = graph.invoke(initial_state)

    return {
        "status": "success",
        "document_title": result["document_title"],
        "document_type": result["document_type"],
        "quality_score": result["quality_score"],
        "reflection_status": result["reflection_status"],
        "feedback": result["reflection_feedback"],
        "execution_plan": [
            task.model_dump()
            for task in result["execution_plan"]
        ],
        "output_file": result["output_file"]
    }