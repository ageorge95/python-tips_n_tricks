from multiprocessing import Process
from time import sleep
from random import randint

def slave_func():
    to_sleep_s = randint(1,30)/10
    sleep(to_sleep_s)
    print(f"I slept for {to_sleep_s} s and finished the task.")

if __name__ == '__main__':
    for _ in range(100):
        Process(target=slave_func,
                args=()).start()