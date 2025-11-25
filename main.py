from agents.orchestrator import Orchestrator
import pprint

def main():
    orchestrator = Orchestrator()
    user_request = {
        "city": "Hyderabad",
        "interests": ["art", "cafes", "photography"],
        "user_id": "demo_user"
    }

    output = orchestrator.run(user_request)
    pprint.pprint(output)

if __name__ == "__main__":
    main()
