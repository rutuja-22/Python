from abc import ABC,abstractmethod

class Computer(ABC):
    @abstractmethod
    def process(self):
        pass

class Laptop(Computer):
    def process(self):
        print("Implementing abstract method")

lap = Laptop()
lap.process()