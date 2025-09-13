# Minimal client (démo). Aucune dépendance externe.
import json
import urllib.request

class Client:
    def __init__(self, api_key: str, base_url: str = "https://api.moodai.dev"):
        self.api_key = api_key
        self.base_url = base_url

    def _post(self, path: str, payload: dict):
        req = urllib.request.Request(
            url=f"{self.base_url}{path}",
            data=json.dumps(payload).encode("utf-8"),
            headers={"Content-Type": "application/json", "Authorization": f"Bearer {self.api_key}"},
            method="POST",
        )
        with urllib.request.urlopen(req) as r:
            return json.loads(r.read().decode("utf-8"))

    def rerank(self, playlist, mood: str):
        return self._post("/rerank", {"playlist": playlist, "mood": mood})

    def feedback(self, data: dict):
        return self._post("/feedback", data)
