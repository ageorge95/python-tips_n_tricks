# !!! IMPORTANT !!!
# abstract method is a method which only has declaration and doesn't have definition.
# a class is called abstract class only if it has at least one abstract method.
# when you inherit a abstract class as a parent to the child class, the child class should define all the abstract method present in parent class.
# if it is not done then child class also becomes abstract class automatically.
# python by default doesn't support abstract class and abstract method, so there is a package called ABC(abstract base classes) by which we can make a class or method abstract

from abc import ABC, abstractmethod

class Computer(ABC):
    @abstractmethod
    def processor(self):
        pass

# cannot instantiate the abstract class Computer directly, it will throw an exception at runtime
# obj = Computer()

# BUT creating a class which inherits the Computer parent class AND has the abstract methods filled out works
class Laptop(Computer):
    def processor(self):
        print('x86')

obj = Laptop()
obj.processor()

# it would not work though if any of the abstract methods are not defined
class Laptop(Computer):
    def RAM(self):
        print(16)

obj = Laptop()
obj.RAM()