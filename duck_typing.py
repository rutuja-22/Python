#duck typing means polymorphism

class Pycharm:
    def execute(self):
        print("Compiling")
        print("Running")

class VS:
    def execute(self):
        print("Spell check")
        print("Compiling")
        print("Running")

class Laptop:
    def code(self,ide):
        ide.execute(self)


#ide = Pycharm()
ide = VS
lap = Laptop()
lap.code(ide)