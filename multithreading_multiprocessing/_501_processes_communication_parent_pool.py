from multiprocessing import Pool
from time import sleep
from random import randint

def slave_func(message):
    to_sleep_s = randint(1,30)/10
    sleep(to_sleep_s)
    # print(f"I slept for {to_sleep_s} s and finished the task.")
    return message

if __name__ == '__main__':

    processes_pool = Pool(processes=5)
    results = []
    for _ in range(10):
        results.append(processes_pool.map(slave_func,
                                          (_,)))
    processes_pool.close()

    for result in results:
        print(result)