import asyncio

async def main():
    task = asyncio.create_task(other_func())
    print("A")
    await asyncio.sleep(1)
    print("B")
    msg = await task
    print(msg)
    
async def other_func():
    print("1")
    await asyncio.sleep(2)
    print("2")
    return "HELLO"

asyncio.run(main())