from time import sleep
from multiprocessing import Queue

def my_process(quit_queue: Queue):
    while True:
        sleep(1)
        print('I am a process and I do stuff :)')
        if not quit_queue.empty():
            print('Exit command received.')
            return