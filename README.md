# MoodAI SDK — v0

## Objectif
Un mini SDK pour tester un service d'IA de re-classement de playlists par "mood".

## Arborescence
moodai-sdk/
  README.md
  python/moodai/__init__.py
  ts/src/client.ts
  examples/python_focus.py
  examples/ts_sport.ts

## Utilisation — Python (Focus)
from moodai import Client
client = Client(api_key="DEMO_KEY", base_url="https://api.moodai.dev")
res = client.rerank(["t1","t2","t3"], mood="focus")
print(res)

## Utilisation — TypeScript (Sport)
import { Client } from "./ts/src/client";
const client = new Client("DEMO_KEY","https://api.moodai.dev");
client.rerank(["t1","t2","t3"], "sport").then(console.log);

## Feedback (exemple Python)
client.feedback({ "user_id": "u_1", "track_id": "t2", "action": "skip", "mood_context": "sport" })
