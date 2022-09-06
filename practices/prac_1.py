import asyncio

async def main():
    task = asyncio.create_task(other_func())
    print("A")
    await asyncio.sleep(1)
    await asyncio.sleep(3)
    print("B")
    
async def other_func():
    print("1")
    await asyncio.sleep(2)
    print("2")

asyncio.run(main())