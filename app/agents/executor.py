from app.prompts.executor_prompt import executor_prompt
from app.services.groq_service import groq_service


class ExecutorAgent:

    def __init__(self):
        self.llm = groq_service.get_llm()

    def generate_sections(
            self,
            request: str,
            document_title: str,
            document_type: str,
            sections: list[str],
            assumptions: list[str],
            feedback: str=""
    ):

        generated_sections = {}

        for section in sections:

            chain = executor_prompt | self.llm

            response = chain.invoke(
                {
                    "request": request,
                    "document_title": document_title,
                    "document_type": document_type,
                    "section": section,
                    "assumptions": ", ".join(assumptions),
                    "feedback": feedback
                }
            )

            generated_sections[section] = response.content

        return generated_sections


executor_agent = ExecutorAgent()