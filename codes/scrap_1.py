import asyncio
import ssl
import aiohttp
import os
import time

from dotenv import load_dotenv
load_dotenv()


api_key = os.getenv("API_KEY")
url =  'https://www.alphavantage.co/query?function=OVERVIEW&symbol={}&apikey={}'

symbols = ['TSLA', "GOOG", "AAPL", "BAC", "BABA"]
results = []

def get_tasks(session):
    tasks = []
    for symbol in symbols:
        tasks.append(asyncio.create_task(session.get(url.format(symbol, api_key), ssl=False)))
    return tasks


async def get_symbols():
    async with aiohttp.ClientSession() as session:
        tasks = get_tasks(session)
        
        res = await asyncio.gather(*tasks)
        
        for r in res:
            results.append(await r.json())
            

asyncio.run(get_symbols())
print(results)