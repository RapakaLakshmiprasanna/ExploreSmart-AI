from agents.orchestrator import Orchestrator
import pprint

def run_demo():
    orch = Orchestrator()
    request = {
        "city": "Hyderabad",
        "interests": ["cafes", "art", "photography"],
        "user_id": "demo_user"
    }
    out = orch.run(request)
    pprint.pprint(out)

if __name__ == "__main__":
    run_demo()
