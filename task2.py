#UDONELS - Task 2
import asyncio
import aiohttp

urls = []
with open("Task 2 - Intern.csv") as f:
    urls = [line.strip() for line in f if line.strip()]

async def fetch_status(session, url):
    try:
        async with session.get(url, timeout=15) as response:
            print(f"({response.status}) {url}")
    except Exception as e:
        print(f"(ERR) {url} — {e.__class__.__name__}")

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_status(session, url) for url in urls]
        await asyncio.gather(*tasks)
        
if __name__ == "__main__":
    asyncio.run(main())
