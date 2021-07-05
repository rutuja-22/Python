def topten():
    n = 1
    while n <= 10:
        sq = n * n
        yield sq           #yield is keyword which makes a function generator
        n += 1

s = topten()

for i in s:
    print(i)