# where you can put await

# async def fib(n):
#     if n<2:
#         return 1
#     else: 
#         return await fib(n-1) + await fib(n-2)


# async def main():
#     for n in range(30):
#         print(await(fib(n)), ", ")

# def run(coroutine):
#     try:
#         coroutine.send(None)
#     except StopIteration as e:
#         return e.value 

    
# run(main())

import time

# def count():
#     time.sleep(1)
#     print('1')
#     time.sleep(1)
#     print('2')
#     time.sleep(1)
#     print('3')
# def main():
#     for i in range(3):
#         count()


# if __name__=='__main__':
#     t1 = time.perf_counter()
#     main()
#     t = time.perf_counter() -t1
#     print(f'Total time = {t:0.2f} sec. ')

### With async 
import asyncio

async def count():
    await asyncio.sleep(1)
    print('1')
    await asyncio.sleep(1)
    print('2')
    await asyncio.sleep(1)
    print('3')
async def main():
    await asyncio.gather(count(), count(), count())


if __name__=='__main__':
    t1 = time.perf_counter()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    t = time.perf_counter() -t1
    print(f'Total time = {t:0.2f} sec. ')
    