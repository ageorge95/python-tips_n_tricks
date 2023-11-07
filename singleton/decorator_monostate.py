def singleton(cls):

    # only 1 initialization at the begining of runtime
    obj = cls()

    def proxy():
        return obj

    return proxy

@singleton
class A:
    def __init__(self,
                 start_counter = 0):
        self.start_counter = start_counter

    def do(self):
        self.start_counter += 1
        print(self.start_counter)

my_obj = A()
my_obj.do()
my_obj2 = A()
my_obj2.do()
my_obj3 = A()
my_obj3.do()