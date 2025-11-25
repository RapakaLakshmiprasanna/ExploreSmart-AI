"""
PreferenceAgent: builds a user preference profile using current request and memory.
"""
from typing import Dict, Any, List
import logging

logger = logging.getLogger(__name__)

class PreferenceAgent:
    def __init__(self):
        pass

    def analyze(self, request: Dict[str, Any], memory_profile: Dict[str, Any]) -> Dict[str, Any]:

        # 1️⃣ Process session interests
        interests = request.get("interests", []) or []

        # Convert string → list safely
        if isinstance(interests, str):
            interests = [i.strip() for i in interests.split(",") if i.strip()]

        # 2️⃣ Load memory interests
        longterm = (memory_profile or {}).get("top_interests", []) or []

        # Ensure memory interests are also a list
        if isinstance(longterm, str):
            longterm = [longterm]

        # 3️⃣ Merge interests without duplicates
        merged: List[str] = []
        for i in interests + longterm:
            if i not in merged:
                merged.append(i)

        # 4️⃣ Build profile
        profile = {
            "top_interests": merged[:5],
            "preferences_meta": {
                "source": "session+memory",
                "session_interests_count": len(interests),
            }
        }

        logger.info("PreferenceAgent: profile=%s", profile)
        return profile
