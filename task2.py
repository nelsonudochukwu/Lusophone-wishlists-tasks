"""
#UDONELS - Task 2
This script reads a list of URLs from a CSV file (skipping the header),
then sends HTTP GET requests to check their status codes asynchronously.

Output format:
(200) http://example.com
(ERR) http://broken-link.com — ConnectionError

Requires:
- aiohttp
- asyncio
"""
import asyncio
import aiohttp

def load_urls(file_path):
    """Loads URLs from a text/CSV file, skipping the first line and keeping only valid http(s) URLs."""
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    # Skip the first line and validate others
    urls = [
        line.strip() for line in lines[1:]  # skip header
        if line.startswith("http")  # keep only valid http(s) links
    ]
    return urls

async def fetch_status(session, url):
    """Fetch the HTTP status code of a given URL using the provided aiohttp session."""
    try:
        async with session.get(url, timeout=15) as response:
            print(f"({response.status}) {url}")
    except Exception as e:
        print(f"(ERR) {url} — {e.__class__.__name__}")

async def main():
    """Main entry point: load URLs and check their status codes concurrently."""
    urls = load_urls("Task 2 - Intern.csv")
    
    # ⚡ Async is ideal here because we're making many I/O-bound (network) requests.
    # Instead of waiting for one URL to respond before requesting the next,
    # asyncio + aiohttp lets us send many requests in parallel, saving time and resources.
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_status(session, url) for url in urls]
        await asyncio.gather(*tasks)
        
if __name__ == "__main__":
    asyncio.run(main())
