import asyncio
import time

async def coroutine_A():
  print('coroutine_A starts!')
  await asyncio.sleep(3)
  print('coroutine_A completed!')

async def coroutine_B():
  print('coroutine_B starts!')
  await asyncio.sleep(2)
  print('coroutine_B completed!')

def main():
  loop = asyncio.get_event_loop()
  tasks = asyncio.gather(
    coroutine_A(),
    coroutine_B()
  )
  loop.run_until_complete(tasks)
  loop.close()

time_start = time.time()
main()
time_end = time.time()

print(f'Took {time_end - time_start}')