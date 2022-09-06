import asyncio

async def fetch_data(): # coroutine
    print("START FETCHING")
    await asyncio.sleep(2)
    print("DONE FETCHING")
    return {"data": 1}

async def print_numbers():
    for i in range(10):
        print(i)
        await asyncio.sleep(.25)

async def main():
    task1 = asyncio.create_task(fetch_data())
    task2 = asyncio.create_task(print_numbers())
    
    value = await task1 
    print(value)
    await task2

asyncio.run(main()) # event loop