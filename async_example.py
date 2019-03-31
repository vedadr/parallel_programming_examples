import asyncio
import random


async def print_info(info):
    print(f'Starting async instance nr. {info}')
    wait = random.randint(3, 10)
    await asyncio.sleep(wait)
    print(f'Async nr. {info} ended after {wait} seconds.')


if __name__ == '__main__':
    loop = asyncio.get_event_loop()

    tasks = []

    for i in range(5):
        tasks.append(print_info(i))

    loop.run_until_complete(asyncio.wait(tasks))
