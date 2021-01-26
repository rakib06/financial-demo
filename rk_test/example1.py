import asyncio

loop = asyncio.get_event_loop()

async def outer():
    print('in outer')
    print('waiting for result1')
    result1 = await phase1()
    print('waiting for result2')
    result2 = await phase2(result1)
    return result1,result2

async def phase1():
    print('in phase1')
    return 'phase1 result'

async def phase2(arg):
    print('in phase2')
    return 'result2 derived from {}'.format(arg)

loop.run_until_complete(outer())
loop.close()

