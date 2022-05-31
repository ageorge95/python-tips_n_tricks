# WARNING: This method is thread safe BUT it is NOT process safe !!!
# Processes have a different address space, to communicate within them, interprocess communication methods need to be used !

from multiprocessing import Manager, Process
from threading import Thread

class Singleton(type):
    '''
    Class which acts as a Singleton if used as a metaclass;
    It is thread safe
    '''
    _instances = {}

    def __call__(cls, *args, **kwargs):

        # example of a shared cache between multiple threads
        if 'shared_cache' not in cls._instances.keys():
            cls._instances['shared_cache'] = Manager().dict()

        if cls not in cls._instances:

            cls.shared_cache = cls._instances['shared_cache']

            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class My_singleton_class(metaclass=Singleton):
    def __init__(self):
        self.my_value = None

    def store_a_value(self,
                      value):
        self.my_value = value

    def get_stored_value(self):
        return self.my_value

def store_value_proxy(value):
    my_obj = My_singleton_class()
    my_obj.store_a_value(value)
    print(f"I have updated the value to {value}")

if __name__ == '__main__':
    my_singleton_obj = My_singleton_class()
    my_singleton_obj.store_a_value(1)
    print(f"Same process, should be 1: {my_singleton_obj.get_stored_value()}")

    t = Thread(target=store_value_proxy,
               args=(2,))
    t.start()
    t.join()

    print(f"Different thread, should be 2: {my_singleton_obj.get_stored_value()}")

    t = Process(target=store_value_proxy,
                args=(3,))
    t.start()
    t.join()

    print(f"Different process, should be 3: {my_singleton_obj.get_stored_value()}")