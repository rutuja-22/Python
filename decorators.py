# in python everything is object that means function is also an object...
# so we can pass function to another function.

def div(a,b):
    print(a/b)

def smart_div(func):
    def inner(a,b):
        if a < b:
            a,b = b,a
        return func(a,b)
    return inner

div = smart_div(div)   #decorators are used to change the behavior of existing function at compile time
div(2,4)
