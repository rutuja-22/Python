from functools import reduce

nums = [3,5,2,6,8,9]

evens = list(filter(lambda a: a%2==0,nums))
print(evens)

doubles = list(map(lambda a: a*2,evens))
print(doubles)

sum = reduce(lambda a,b: a+b,doubles)   #for reduce func we need functools
print(sum)

test = list(map(lambda a: a+2,evens))
print(test)