#UDONELS - Task 2
import asyncio
import aiohttp
import csv

def load_urls(file_path):
    """Loads URLs from a text/CSV file, skipping the first line and keeping only valid http(s) URLs."""
    urls = []
    with open(file_path, 'r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        next(csv_reader) # Skip the header
        urls = [row[0] for row in csv_reader]
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
