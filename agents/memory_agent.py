"""
MemoryAgent: in-memory session + simple file-based long-term storage (mock).
"""
import json
from pathlib import Path
from typing import Dict, Any
import logging

logger = logging.getLogger(__name__)

DB_PATH = Path("./.mock_memory")
DB_PATH.mkdir(exist_ok=True)

class MemoryAgent:
    def __init__(self):
        self.session = {}
        self.user_profile = {}

    def load_user_profile(self, user_id: str) -> Dict[str, Any]:
        fp = DB_PATH / f"{user_id}.json"
        if fp.exists():
            try:
                data = json.loads(fp.read_text())
                self.user_profile = data
                logger.info("MemoryAgent: loaded profile for %s", user_id)
            except Exception as e:
                logger.warning("MemoryAgent: failed to read profile: %s", e)
                self.user_profile = {}
        else:
            self.user_profile = {}
        return self.user_profile

    def update_session(self, data: Dict[str, Any]):
        self.session.update(data)
        logger.info("MemoryAgent: session updated")

    def save_user_profile(self, user_id: str, profile: Dict[str, Any]) -> bool:
        fp = DB_PATH / f"{user_id}.json"
        try:
            fp.write_text(json.dumps(profile, indent=2))
            logger.info("MemoryAgent: saved profile for %s", user_id)
            return True
        except Exception as e:
            logger.error("MemoryAgent: failed to save profile: %s", e)
            return False
