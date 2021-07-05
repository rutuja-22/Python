class TopTen:
    def __init__(self):
        self.num = 1
    def __iter__(self):   #iter return the iteration object
        return self
    def __next__(self):   #next is method for iterating the value
        if self.num<=10:
            val = self.num
            self.num += 1

            return val
        else:
            raise StopIteration
s = TopTen()
for i in s:
    print(i)
