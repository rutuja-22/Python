def linear(num,key):
    for i in range(len(num)):
        if num[i] == key:
            return i+1
    return -1 

nums = [56,26,38,84,15]
print(nums)
key = int(input("Enter value to search: "))
x = linear(nums,key)
if(x==-1):
    print("Key not found..")
else:
    print("Given key ",key,"is found at position: ",x)


