from agents.orchestrator import Orchestrator

def test_run_returns_itinerary():
    orch = Orchestrator()
    request = {"city": "Hyderabad", "interests": ["art"], "user_id": "test_user"}
    out = orch.run(request)
    assert "itinerary" in out
    assert isinstance(out["itinerary"], list)
    assert out["user_id"] == "test_user"
