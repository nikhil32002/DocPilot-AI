import logging

from app.prompts.planner_prompt import planner_prompt
from app.services.groq_service import groq_service
from app.services.parser_service import planner_parser

logger = logging.getLogger(__name__)


class PlannerAgent:

    def __init__(self):
        self.llm = groq_service.get_llm()

    def plan(self, request: str):

        logger.info("Planner started")

        chain = (
                planner_prompt
                | self.llm
                | planner_parser
        )

        result = chain.invoke(
            {
                "request": request
            }
        )

        logger.info("Planner completed")

        return result


planner_agent = PlannerAgent()