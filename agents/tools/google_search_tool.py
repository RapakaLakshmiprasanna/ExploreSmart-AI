"""
Mock Google Search tool.
Replace with real API or ADK tool integration later.
"""
from typing import List, Dict
import random

class GoogleSearchTool:
    def __init__(self):
        pass

    def search(self, query: str, max_results: int = 5) -> List[Dict]:
        # deterministic-ish mocked results for local testing
        mock = []
        base_lat = 17.4
        base_lng = 78.4
        for i in range(max_results):
            idx = abs(hash(query)) % 100 + i
            mock.append({
                "name": f"Hidden Spot {idx} ({query})",
                "address": f"Street {idx}, {query.split()[-1]}",
                "lat": round(base_lat + (i * 0.01), 6),
                "lng": round(base_lng + (i * 0.01), 6),
                "snippet": f"A cozy off-beat place related to {query}.",
                "score": random.randint(30, 90),
                "popularity_score": random.randint(10, 80),
            })
        return mock
