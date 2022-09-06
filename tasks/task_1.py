import asyncio

async def fetch(url):
    print(f"Fetching {url}")
    await asyncio.sleep(1)
    return {
        "url": url
    }

async def main():
    # all the fetches are called at once until they meet the await
    data = await asyncio.gather(
        fetch("1st url"),
        fetch("2nd url"),
        fetch("3rd url"),
        fetch("4th url"),
        fetch("5th url"),
    )

    print(data)

asyncio.run(main()) 