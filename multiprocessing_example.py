import multiprocessing
import random
import time


def print_info(info):
    print(f'Process {info} started!')
    wait = random.randint(3, 10)
    time.sleep(wait)
    print(f'Process {info} ended after {wait} seconds!')


if __name__ == '__main__':
    for i in range(5):
        multiprocessing.Process(target=print_info, args=[i]).start()
