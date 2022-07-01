from multiprocessing import Process
from time import sleep
from random import randint
from custom_logger.custom_logger_vanilla import configure_logger
from logging import getLogger

def slave_func():
    configure_logger()
    _log = getLogger()

    to_sleep_s = randint(1,30)/10
    sleep(to_sleep_s)
    _log.info(f"I slept for {to_sleep_s} s and finished the task.")

if __name__ == '__main__':
    for _ in range(100):
        Process(target=slave_func,
                args=()).start()