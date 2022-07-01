from threading import Thread
from multiprocessing import Manager
from time import sleep
from random import randint

def slave_func(thread_ID,
               cache):
    to_sleep_s = randint(1,30)/10
    sleep(to_sleep_s)
    # print(f"I slept for {to_sleep_s} s and finished the task.")
    if cache['biggest_thread_ID'] < thread_ID:
        cache['biggest_thread_ID'] = thread_ID
        cache['changed_by_ID'] = thread_ID

if __name__ == '__main__':
    manager = Manager()
    cache = manager.dict({'biggest_thread_ID': 0,
                          'changed_by_ID': 0})
    # cache = {'biggest_thread_ID': 0,
    #          'changed_by_ID': 0}

    for _ in range(100):
        Thread(target=slave_func,
               args=(_,
                     cache,)).start()

    print('threads_not_finished', cache)

    sleep(4)
    print('threads_finished', cache)

