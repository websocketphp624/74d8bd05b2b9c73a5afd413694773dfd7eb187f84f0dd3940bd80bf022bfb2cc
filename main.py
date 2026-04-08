"""coordinator_4301bb - Simple checker."""
import urllib.request, sys, time
SERVICE_TAG = "coordinator_4301bb"
TARGETS = ["https://httpbin.org/status/200", "https://example.com"]
def check(url: str) -> dict:
    try:
        start = time.time()
        req = urllib.request.Request(url, method="HEAD")
        with urllib.request.urlopen(req, timeout=5) as resp:
            elapsed = time.time() - start
            return {"url": url, "status": resp.status, "time_ms": int(elapsed * 1000)}
    except Exception as e:
        return {"url": url, "status": -1, "error": str(e)}
def main():
    print(f"[{SERVICE_TAG}] Running checks...")
    for url in TARGETS:
        result = check(url)
        print(f"  {result}")
    print(f"[{SERVICE_TAG}] Done.")
if __name__ == "__main__":
    main()
