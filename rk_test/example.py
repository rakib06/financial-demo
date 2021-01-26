import asyncio

async def greeter(name):
    print('Hi', name, " you're in a coroutine." )

# for python 3.6
# loop = asyncio.get_event_loop()
# loop.run_until_complete(greeter('RK'))
# loop.close()

loop = asyncio.get_event_loop()
try:
    print("Starting coroutine...")
    coro = greeter('RK')
    print('Entering event loop..')
    loop.run_until_complete(coro)
finally:
    print("Closing event loop")
    loop.close()
