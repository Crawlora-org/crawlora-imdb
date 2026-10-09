import { IMDbClient } from "../src/index.js";

const client = new IMDbClient({ apiKey: "test-key" });
void client.search({"query": "sample"});
void client.request("imdb-search", {"query": "sample"});
const streamResponse: Promise<Response> = client.request("imdb-search", {"query": "sample"}, { responseType: "stream" });
const operationStream: Promise<Response> = client.operation("imdb-search", {"query": "sample"}, { responseType: "stream" });
const directStream: Promise<Response> = client.search({"query": "sample"}, { responseType: "stream" });
void streamResponse; void operationStream; void directStream;
void client.request("imdb-search", {"query": "sample", "limit": 1}, { responseType: "text" });
const rawText: Promise<string> = client.request("imdb-search", {"query": "sample"}, { responseType: "text" });
void rawText;


void client.charts();
void client.request("imdb-charts");
// @ts-expect-error The selected operation requires its documented params.
void client.search();
