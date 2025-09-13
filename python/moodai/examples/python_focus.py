from moodai import Client
client = Client(api_key="DEMO_KEY", base_url="https://api.moodai.dev")
print(client.rerank(["t1","t2","t3"], mood="focus"))
