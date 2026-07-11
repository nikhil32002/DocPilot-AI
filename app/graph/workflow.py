from langgraph.graph import StateGraph, END

from app.graph.state import AgentState

from app.agents.planner import planner_agent
from app.agents.executor import executor_agent
from app.agents.reflector import reflection_agent

from app.services.doc_generator import document_generator

def planner_node(state: AgentState):

    plan = planner_agent.plan(state["request"])

    state["document_title"] = plan.document_title
    state["document_type"] = plan.document_type
    state["assumptions"] = plan.assumptions
    state["sections"] = plan.sections
    state["execution_plan"] = plan.execution_plan

    return state

def executor_node(state: AgentState):

    sections = executor_agent.generate_sections(
        request=state["request"],
        document_title=state["document_title"],
        document_type=state["document_type"],
        assumptions=state["assumptions"],
        sections=state["sections"],
        feedback=state.get("reflection_feedback", "")
    )

    state["generated_sections"] = sections

    return state

def reflection_node(state: AgentState):

    document = "\n\n".join(
        f"{heading}\n{content}"
        for heading, content in state["generated_sections"].items()
    )

    review = reflection_agent.review(document)

    state["quality_score"] = review.quality_score
    state["reflection_feedback"] = review.feedback

    if review.quality_score >= 85:
        state["reflection_status"] = "PASS"
    else:
        state["reflection_status"] = "FAIL"

    return state

def reflection_router(state: AgentState):

    if state["reflection_status"] == "PASS":
        return "docx"

    if state["retry_count"] >= 1:
        return "docx"

    state["retry_count"] += 1

    return "executor"

def docx_node(state: AgentState):

    output_file = document_generator.generate(
        title=state["document_title"],
        sections=state["generated_sections"],
    )

    state["output_file"] = output_file

    return state

workflow = StateGraph(AgentState)

workflow.add_node("planner", planner_node)
workflow.add_node("executor", executor_node)
workflow.add_node("reflection", reflection_node)
workflow.add_node("docx", docx_node)

workflow.set_entry_point("planner")

workflow.add_edge("planner", "executor")
workflow.add_edge("executor", "reflection")
workflow.add_conditional_edges(
    "reflection",
    reflection_router,
    {
        "executor": "executor",
        "docx": "docx",
    },
)
workflow.add_edge("docx", END)

graph = workflow.compile()