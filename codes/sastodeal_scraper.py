import asyncio
import aiohttp
import requests
from bs4 import BeautifulSoup as bs

query = "Fantech Headphones"
params = {
    "q": query
}
url = f"https://www.sastodeal.com/catalogsearch/result/"

def get_urls():
    res =requests.get(url, params=params)
    soup = bs(res.content, "html.parser")
    items = soup.find_all("a", class_="product-item-link")
    urls = [item.get("href") for item in items if item.get("href")]
    return urls
    
async def get_page(session, url):
    async with session.get(url) as res:
        return await res.text()

async def get_all(session, urls):
    tasks = []
    for url in urls:
        task = asyncio.create_task(get_page(session, url))
        tasks.append(task)
    results = await asyncio.gather(*tasks)
    return results

async def main(urls):
    async with aiohttp.ClientSession() as session:
        data = await get_all(session, urls)
        return data
    

if __name__ == "__main__":
    urls = get_urls()
    data = asyncio.run(main(urls))
    print(data)