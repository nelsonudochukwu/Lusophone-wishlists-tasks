#UDONELS - Task 2
import asyncio
import aiohttp

def load_urls(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    # Skip the first line and validate others
    urls = [
        line.strip() for line in lines[1:]  # skip header
        if line.startswith("http")  # keep only valid http(s) links
    ]
    return urls

async def fetch_status(session, url):
    try:
        async with session.get(url, timeout=15) as response:
            print(f"({response.status}) {url}")
    except Exception as e:
        print(f"(ERR) {url} — {e.__class__.__name__}")

async def main():
    urls = load_urls("Task 2 - Intern.csv")
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_status(session, url) for url in urls]
        await asyncio.gather(*tasks)
        
if __name__ == "__main__":
    asyncio.run(main())
