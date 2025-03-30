#UDONELS - Task 2
import asyncio
import aiohttp
import csv

def load_urls(file_path):
    """
    Loads URLs from a CSV file
    
    Args:
        - file_path : csv file containing urls to be read
    Returns:
        - List of urls read from the csv_file
    """
    urls = []
    with open(file_path, 'r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        next(csv_reader) # Skip the header
        urls = [row[0] for row in csv_reader]
    return urls

async def fetch_status(session, url):
    """
    Fetch the HTTP status code of a given URL using the provided aiohttp session
    
    Args:
        - session: session for making http requests
        - url (string): url to which a request is to be made
    Prints:
        - (STATUS CODE) URL : when a request is successfully made
        - (ERR) URL - ErrorType: when a request connection to the url fails
    """
    try:
        async with session.get(url, timeout=15) as response:
            print(f"({response.status}) {url}")
    except Exception as e:
        print(f"(ERR) {url} — {e.__class__.__name__}")

async def main():
    """
    Main entry point: load URLs and check their status codes concurrently.
    """
    urls = load_urls("Task 2 - Intern.csv")
    
    # Async helps us to save time and resources by making I/O-bound (network) requests in parallel 
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_status(session, url) for url in urls]
        await asyncio.gather(*tasks)
        
if __name__ == "__main__":
    asyncio.run(main())

