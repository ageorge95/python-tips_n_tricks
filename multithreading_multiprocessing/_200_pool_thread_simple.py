from concurrent.futures import ThreadPoolExecutor
from time import sleep
from random import randint

def slave_func():
    to_sleep_s = randint(1,30)/10
    sleep(to_sleep_s)
    print(f"I slept for {to_sleep_s} s and finished the task.")

threads_pool = ThreadPoolExecutor(max_workers=10)
for _ in range(100):
    threads_pool.submit(slave_func)
threads_pool.shutdown()