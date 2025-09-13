// Minimal client (démo)
export class Client {
  constructor(private apiKey: string, private baseUrl: string = "https://api.moodai.dev") {}

  private async post(path: string, payload: any) {
    const res = await fetch(this.baseUrl + path, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "Authorization": `Bearer ${this.apiKey}`
      },
      body: JSON.stringify(payload)
    });
    return await res.json();
  }

  async rerank(playlist: string[], mood: "focus"|"sport"|"chill"|"joy"|"sad") {
    return this.post("/rerank", { playlist, mood });
  }

  async feedback(data: { user_id: string; track_id: string; action: "skip"|"like"|"finish"; mood_context?: string; rating?: number }) {
    return this.post("/feedback", data);
  }
}
