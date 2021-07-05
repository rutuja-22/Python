
a = 5
b = 0

try:
    print("resource open")
    print(a/b)
    k =int(input(" Enter a number: "))
    print(k)
except ZeroDivisionError as e:
    print("Cannot divide by zero...",e)
except ValueError as e:
    print("Invalid input...",e)
except Exception as e:
    print("Somethinf went wrong..",e)
finally:
    print("resource closed")
print("All are done")