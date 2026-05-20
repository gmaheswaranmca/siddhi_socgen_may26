##  Using async and await features to implement co-routines and concurrency patterns.
    #  An overview on the asyncio library.
import asyncio

# coroutine
async def download_file(file_name, seconds):
    print(f"Started downloading {file_name}")

    # non-blocking wait
    await asyncio.sleep(seconds)

    print(f"Completed downloading {file_name}")


# main coroutine
async def main():
    print("Download Started")
    # concurrency using asyncio
    await asyncio.gather(
        download_file("python.pdf", 3),
        download_file("react.pdf", 2),
        download_file("go.pdf", 1)
    )
    print("All Downloads Completed")

# event loop execution
asyncio.run(main())