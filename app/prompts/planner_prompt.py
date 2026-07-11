from langchain_core.prompts import ChatPromptTemplate

from app.services.parser_service import planner_parser

planner_prompt = ChatPromptTemplate.from_template(
"""
You are an autonomous AI Planning Agent.

Your ONLY responsibility is planning.

Do NOT generate document content.

Analyze the user's request.

Determine

- document title
- document type
- assumptions
- sections
- execution tasks

{format_instructions}

User Request

{request}

"""
).partial(
    format_instructions=planner_parser.get_format_instructions()
)