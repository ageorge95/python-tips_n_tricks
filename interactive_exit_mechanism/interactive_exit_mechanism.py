from threading import Thread
from multiprocessing import Process,\
    Queue
from time import sleep
from sys import stdin
from my_separate_process import my_process

def read_input(quit_queue: Queue):
    input_data = ''
    while True:
        sleep(0.5)
        input_data += stdin.read(1).strip()
        input_data = input_data[-10:]
        if input_data.endswith('exit'):
            quit_queue.put(1)
            print('EXIT COMMAND PROPAGATED !')
            return

if __name__ == '__main__':
    QuitQueue = Queue()
    Process(target=my_process,
            args=(QuitQueue,)).start()
    Thread(target=read_input,
           args=(QuitQueue,)).start()