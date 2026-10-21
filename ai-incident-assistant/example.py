import asyncio

async def fetch_log(log_id):
    print(f"Started fetching log {log_id}")

    await asyncio.sleep(2)
    
    print(f"Finished fetching log {log_id}")

    return f"Log {log_id} fetched"

async def main():
    result = await fetch_log(1)
    print(result)

asyncio.run(main())