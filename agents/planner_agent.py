"""
PlannerAgent: creates time-ordered itinerary, calculates map links.
"""
from agents.tools.maps_tool import MapsTool
from typing import List, Dict
import logging

logger = logging.getLogger(__name__)

class PlannerAgent:
    def __init__(self):
        self.maps = MapsTool()

    def create_itinerary(self, places: List[Dict], profile: Dict) -> List[Dict]:
        logger.info("PlannerAgent: creating itinerary for %d places", len(places))
        # sort by 'score' if present; else keep original order
        sorted_places = sorted(places, key=lambda p: p.get("score", 0), reverse=True)

        itinerary = []
        # simple split into morning/evening alternating
        for idx, place in enumerate(sorted_places[:10]):
            when = "Morning" if idx % 2 == 0 else "Evening"
            lat = place.get("lat")
            lng = place.get("lng")
            itinerary.append({
                "order": idx + 1,
                "time_block": when,
                "name": place.get("name"),
                "address": place.get("address"),
                "maps_url": self.maps.generate_link(lat, lng),
                "short_desc": place.get("snippet"),
                "estimated_visit_mins": 45
            })

        logger.info("PlannerAgent: itinerary length=%d", len(itinerary))
        return itinerary
