"""
SearchAgent: uses tools to discover hidden places.
Mocked implementation returns deterministic sample places.
"""
from agents.tools.google_search_tool import GoogleSearchTool
from typing import List, Dict
import logging

logger = logging.getLogger(__name__)

class SearchAgent:
    def __init__(self):
        self.tool = GoogleSearchTool()

    def search(self, city: str, profile: Dict) -> List[Dict]:
        logger.info("SearchAgent: searching for city=%s profile=%s", city, profile.get("top_interests"))
        queries = []
        for interest in profile.get("top_interests", []):
            queries.append(f"hidden {interest} spots in {city}")

        results = []
        for q in queries:
            results.extend(self.tool.search(q, max_results=5))

        # basic dedupe & filter: remove very popular places (popularity_score > 90)
        seen = set()
        processed = []
        for r in results:
            key = (r.get("name"), r.get("address"))
            if key in seen:
                continue
            seen.add(key)
            if r.get("popularity_score", 0) > 90:
                # skip mainstream
                continue
            processed.append(r)

        logger.info("SearchAgent: returning %d places", len(processed))
        return processed
