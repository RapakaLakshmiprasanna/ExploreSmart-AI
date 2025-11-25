"""
Orchestrator: coordinates sub-agents in a sequential workflow.
"""
from typing import Dict, Any
from agents.search_agent import SearchAgent
from agents.preference_agent import PreferenceAgent
from agents.planner_agent import PlannerAgent
from agents.memory_agent import MemoryAgent
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

class Orchestrator:
    def __init__(self, config: Dict[str, Any]=None):
        self.search_agent = SearchAgent()
        self.pref_agent = PreferenceAgent()
        self.planner_agent = PlannerAgent()
        self.memory_agent = MemoryAgent()

    def run(self, request: dict) -> dict:
        logger.info("Orchestrator: start run")

        user_id = request.get("user_id", "anonymous")
        # 1) load memory
        memory_profile = self.memory_agent.load_user_profile(user_id)
        logger.info("Loaded memory for user %s: %s", user_id, bool(memory_profile))

        # 2) update session context
        self.memory_agent.update_session(request)

        # 3) build preference profile
        preference_profile = self.pref_agent.analyze(request, memory_profile)

        # 4) search hidden gems
        raw_places = self.search_agent.search(request.get("city", ""), preference_profile)

        # 5) plan itinerary
        itinerary = self.planner_agent.create_itinerary(raw_places, preference_profile)

        # 6) persist preferences back to memory
        self.memory_agent.save_user_profile(user_id, preference_profile)

        result = {
            "user_id": user_id,
            "preferences": preference_profile,
            "places_found": len(raw_places),
            "itinerary": itinerary,
        }

        logger.info("Orchestrator: finished run")
        return result
