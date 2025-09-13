import { Client } from "../ts/src/client";
const client = new Client("DEMO_KEY","https://api.moodai.dev");
client.rerank(["t1","t2","t3"], "sport").then(r => console.log(r));
