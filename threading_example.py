import random
import time

import threading


def print_basic_info(ind):
    print(f'Thread {ind} started!')
    wait = random.randint(3, 10)
    time.sleep(wait)
    print(f'Thread {ind} ended after {wait} seconds!')


if __name__ == '__main__':

    for i in range(5):
        threading.Thread(target=print_basic_info, args=[i]).start()

