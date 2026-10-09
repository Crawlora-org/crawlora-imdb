import test from "node:test";
import assert from "node:assert/strict";
import {
  IMDbClient, CrawloraClientError, CrawloraNetworkError,
  CrawloraServerError, groups, operations, operationCount
} from "../src/index.js";

const json = (data, status = 200, headers = {}) => new Response(JSON.stringify(data), {
  status, headers: { "content-type": "application/json", ...headers }
});

test("exports only this platform and exposes direct and grouped methods", async () => {
  const client = new IMDbClient({ apiKey: "test-key", fetch: async () => json({ ok: true }) });
  assert.equal(operationCount, Object.keys(operations).length);
  assert.deepEqual(Object.keys(groups), ["imdb"]);
  assert.equal(typeof client["search"], "function");
  assert.equal(typeof client["imdb"]["search"], "function");
});

test("serializes required query/path values, adds API key and platform User-Agent", async () => {
  let seen;
  const client = new IMDbClient({ apiKey: "secret", fetch: async (url, init) => {
    seen = { url: String(url), headers: init.headers };
    return json({ ok: true });
  } });
  await client.request("imdb-search", {"query": "sample"});
  assert.match(seen.url, /\/imdb\/search/);
  assert.equal(seen.headers["x-api-key"], "secret");
  assert.equal(seen.headers["user-agent"], "crawlora-imdb-js/0.1.0");
});

test("allows caller User-Agent override and response text mode", async () => {
  let seen;
  const client = new IMDbClient({ apiKey: "key", userAgent: "custom-agent", fetch: async (_url, init) => {
    seen = init.headers;
    return new Response("caption text", { headers: { "content-type": "text/plain" } });
  } });
  const result = await client.request("imdb-search", {"query": "sample"}, { responseType: "text" });
  assert.equal(seen["user-agent"], "custom-agent");
  assert.equal(result, "caption text");

  const rawFeed = "1~home|2~away\n";
  const autoClient = new IMDbClient({ fetch: async () => new Response(rawFeed, {
    headers: { "content-type": "text/plain" }
  }) });
  assert.equal(await autoClient.request("imdb-search", {"query": "sample"}), rawFeed);
});

test("maps API errors and retries server failures", async () => {
  let calls = 0;
  const client = new IMDbClient({ apiKey: "key", retries: 1, retryDelay: 0, fetch: async () => {
    calls++;
    return calls === 1 ? json({ msg: "try again" }, 503) : json({ ok: true });
  } });
  assert.deepEqual(await client.request("imdb-search", {"query": "sample"}), { ok: true });
  assert.equal(calls, 2);

  const bad = new IMDbClient({ fetch: async () => json({ msg: "bad input" }, 400) });
  await assert.rejects(bad.request("imdb-search", {"query": "sample"}), CrawloraClientError);
  const down = new IMDbClient({ fetch: async () => json({ msg: "down" }, 503) });
  await assert.rejects(down.request("imdb-search", {"query": "sample"}), CrawloraServerError);
});

test("reports timeout and caller cancellation as network errors", async () => {
  const hanging = (_url, { signal }) => new Promise((_resolve, reject) => {
    signal.addEventListener("abort", () => reject(new Error("aborted")), { once: true });
  });
  const timed = new IMDbClient({ timeout: 5, fetch: hanging });
  await assert.rejects(timed.request("imdb-search", {"query": "sample"}), CrawloraNetworkError);

  const controller = new AbortController();
  const aborted = new IMDbClient({ fetch: hanging });
  const pending = aborted.request("imdb-search", {"query": "sample"}, { signal: controller.signal });
  controller.abort();
  await assert.rejects(pending, CrawloraNetworkError);
});
