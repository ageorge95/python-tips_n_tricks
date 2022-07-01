from threading import Thread
from time import sleep
from random import randint

def slave_func(thread_ID):
    global last_thread
    to_sleep_s = randint(1,30)/10
    sleep(to_sleep_s)
    # print(f"I slept for {to_sleep_s} s and finished the task.")
    last_thread = thread_ID

last_thread = 0
for _ in range(100):
    Thread(target=slave_func,
           args=(_,)).start()

for _ in [0.05]*50:
    print(last_thread)
    sleep(_)