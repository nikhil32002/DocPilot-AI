from app.prompts.reflection_prompt import reflection_prompt
from app.services.groq_service import groq_service
from app.services.reflection_parser import reflection_parser


class ReflectionAgent:

    def __init__(self):
        self.llm = groq_service.get_llm()

    def review(self, document: str):

        chain = (
                reflection_prompt
                | self.llm
                | reflection_parser
        )

        review = chain.invoke(
            {
                "document": document
            }
        )

        return review

reflection_agent = ReflectionAgent()