from concurrent.futures import ThreadPoolExecutor
from time import sleep
from random import randint

def slave_func(message):
    to_sleep_s = randint(1,30)/10
    sleep(to_sleep_s)
    # print(f"I slept for {to_sleep_s} s and finished the task.")
    return message

threads_pool = ThreadPoolExecutor(max_workers=10)
results = []
for _ in range(50):
    results.append(threads_pool.submit(slave_func,
                                       (_)))
threads_pool.shutdown()

for result in results:
    print(result.result())