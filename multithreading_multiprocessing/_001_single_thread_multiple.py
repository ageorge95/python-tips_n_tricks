from threading import Thread
from time import sleep
from random import randint

def slave_func():
    to_sleep_s = randint(1,30)/10
    sleep(to_sleep_s)
    print(f"I slept for {to_sleep_s} s and finished the task.")

for _ in range(100):
    Thread(target=slave_func,
           args=()).start()