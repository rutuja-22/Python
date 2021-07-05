def fib(n):
    a = 0
    b = 1
    if n > 0:
        if n == 1:
            print(a,end = " ")
            return
        if n == 2:
            print(a,b,end = " ")
            return
        print(a,b,end = " ")
        for i in range(2,n):
            c = a + b
            a = b 
            b = c
            print(c,end = " ")
    else: 
        print("Invalid number")       

n = int(input("Enter a number upto which you want fibonacci series: "))
fib(n)

print("\n************************************************************")

def fib(n):
    a = 0
    b = 1
    if n > 0:
        if n == 1:
            print("Fibonacci number at ",n,"is ",a,end = " ")
            return
        if n == 2:
            print("Fibonacci number at ",n,"is ",b,end = " ")
            return
        #print(a,b,end = " ")
        for i in range(2,n):
            c = a + b
            a = b 
            b = c
        print("Fibonacci number at ",n,"is ",c,end = " ")
    else: 
        print("Invalid number")       

n = int(input("Enter a number which you want it's fibonacci number : "))
fib(n)

print("\n************************************************************")