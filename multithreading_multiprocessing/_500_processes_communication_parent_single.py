from multiprocessing import Process,\
    Manager
from time import sleep
from random import randint

def slave_func(thread_ID,
               cache):
    to_sleep_s = randint(1,30)/10
    sleep(to_sleep_s)
    # print(f"I slept for {to_sleep_s} s and finished the task.")
    cache['stored_value'] = thread_ID

if __name__ == '__main__':
    manager = Manager()
    cache = manager.dict({'stored_value': 0})

    for _ in range(50):
        Process(target=slave_func,
                args=(_,
                      cache,)).start()

    print('after the processes have been submitted', cache)

    sleep(5)

    print('some time after that', cache)