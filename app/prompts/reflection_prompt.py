from langchain_core.prompts import ChatPromptTemplate

from app.services.reflection_parser import reflection_parser

reflection_prompt = ChatPromptTemplate.from_template(
"""
You are a senior business document reviewer.

Review the generated business document.

Evaluate:

- Completeness
- Professional tone
- Grammar
- Logical flow
- Business value

Assign an overall quality score between 0 and 100.

If there are no missing sections, return an empty list.

Return ONLY valid JSON.

{format_instructions}

Document:

{document}
"""
).partial(
    format_instructions=reflection_parser.get_format_instructions()
)