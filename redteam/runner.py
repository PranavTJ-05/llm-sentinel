from fastapi.testclient import TestClient
from app.main import app
from redteam.attacks import ATTACKS

client = TestClient(app)

def run_suite(mode: str = "vulnerable") -> list[dict]:
    results = []
    for attack in ATTACKS:
        response = client.post("/chat", json={
            "tenant_id": "acme",
            "user_id": "alice",
            "message": attack.message,
            "mode": mode,
        })
        body = response.json()
        results.append({
            "case_id": attack.case_id,
            "category": attack.category,
            "mode": mode,
            "http_status": response.status_code,
            "reply": body["reply"],
            "tool_executed": body["tool_executed"],
            "evidence": body["evidence"],
        })
    return results

if __name__ == "__main__":
    import json
    print(json.dumps({
        "vulnerable": run_suite("vulnerable"),
        "secure": run_suite("secure"),
    }, indent=2))
