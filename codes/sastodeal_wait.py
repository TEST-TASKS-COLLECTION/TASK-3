import asyncio
import aiohttp
import requests
import time
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
    
    # fault url
    urls.append(f"https://www.sastodeal.com/catalogsearch/wrmg/")
    return urls
    
async def get_page(session, url):
    return await session.get(url)
    # async with session.get(url) as res:
    #     return await res.text()
    #     return res
        # print(res)

async def get_all(session, urls):
    tasks = []
    for url in urls:
        task = asyncio.create_task(get_page(session, url))
        tasks.append(task)
    done, _ = await asyncio.wait(tasks, return_when=asyncio.ALL_COMPLETED)
    results = [d.result() for d in done]
    # done, pending = await asyncio.wait(pending, return_when=asyncio.ALL_COMPLETED)
    # print("*"*15)
    # print(done, pending)
    # print("*"*15)
    return results

def parse_data(data):
    soup = bs(data, "html.parser")
    # print(soup.find("h1", class_="page-title"))
    return soup.select_one(".page-title > span")

async def main(urls):
    async with aiohttp.ClientSession() as session:
        data = await get_all(session, urls)
        # data = [parse_data(await d.text()).text for d in data if parse_data(await d.text())]
        data = [parse_data(await d.text()) for d in data]
        return data
    
if __name__ == "__main__":
    urls = get_urls()
    then = time.time()
    data = asyncio.run(main(urls))
    after = time.time()
    print(data)
    print(f"IT TOOK {after - then}")