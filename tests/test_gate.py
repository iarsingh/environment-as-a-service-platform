from fastapi.testclient import TestClient
from eaas.main import app

client = TestClient(app)


def test_pass_and_fail():
    good = client.post("/check", json={'owner': 'ada', 'ttl_hours': 24}).json()
    assert good["passed"] is True
    assert good["applied"] is False
    bad = client.post("/check", json={'owner': 'ada', 'ttl_hours': 200}).json()
    assert bad["passed"] is False
    assert "ttl" in bad["failed"]
