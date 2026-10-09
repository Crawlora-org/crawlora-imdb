import { IMDbClient } from "../javascript/src/index.js";

const apiKey = process.env.CRAWLORA_API_KEY;
if (!apiKey) throw new Error("Set CRAWLORA_API_KEY before running this example.");
const client = new IMDbClient({ apiKey });

  const search = await client.search({ query: "Inception" });
  console.log("search", search);
  const charts = await client.charts({  });
  console.log("charts", charts);
