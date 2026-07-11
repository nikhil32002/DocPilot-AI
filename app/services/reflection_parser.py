from langchain_core.output_parsers import PydanticOutputParser

from app.models.reflection_output import ReflectionOutput

reflection_parser = PydanticOutputParser(
    pydantic_object=ReflectionOutput
)