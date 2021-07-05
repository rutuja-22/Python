def add_sub(x,y):
    a = x + y
    b = x - y
    return a,b

r1,r2= add_sub(10,5)
print(r1,r2)
print('*****************************************************************')
def update(x):
    print(id(x))
    x = 8
    print("x ",x)
    print(id(x))
a = 10
print(id(a))
update(a)
print("a ",a)

def update(lst):
    print(id(lst))
    lst[1] = 25
    print("lst ",lst)
    print(id(lst))
lst = [10,20,30]
print(id(lst))
update(lst)
print("lst ",lst)

print('*****************************************************************')
def person(name,age=18):
    print(name)
    print(age)
person('rutu',20)  #normal
person(age = 20,name = 'rutu') #keyword
person('rutu')  #default

def sum(a,*b):
    c = a
    for i in b:
        c = c + i
    print("a =",a)
    print("b = ",b)
    print("c=",c)

sum(5,1,2,3)
print('*****************************************************************')

def person(name,**data):
    print(name)
    print(data)
    for i,j in data.items():   #simple data give error ....too many data to fetch
        print(i,j)
person('Rutu',age = 20,city = 'Amt',mob = '8975458575')

print('*****************************************************************')

x = 10

def try_global():
    x = 9
    z = globals()['x']
    print("z =", z)
    print(id(z))
    print("in func = ",x)
    globals()['x'] = 15
try_global()
print("outside = ",x)
print('*****************************************************************')

def count(lst):
    even = 0
    odd = 0
    for i in lst:
        if(i % 2 == 0):
            even = even + 1
        else:
            odd += 1
    return even ,odd
lst = [23,56,34,67,89,67]
even,odd = count(lst)
print("Even = {} Odd = {}".format(even,odd))
print('*****************************************************************')

def func(lst1):
    count = 0
    #length = len(lst1)
    #print(lst1)
    for word in (lst1):
        print (word)
        if(len(word) >3):
            count+=1
    return count

#lst1 = input("Enter 10 names:")   #not working
lst1 = ['rutu','ru','rtrg']
result = func(lst1)
print("Names having greater then 3 letters are: ",result)
print('*****************************************************************')

