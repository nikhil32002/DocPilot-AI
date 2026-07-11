from langchain_core.output_parsers import PydanticOutputParser

from app.models.planner_output import PlannerOutput

planner_parser = PydanticOutputParser(
    pydantic_object=PlannerOutput
)