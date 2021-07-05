def binary(num,key):
    beg = 0
    end = len(num)-1 
    while beg<=end:
        mid = (beg + end)//2
        if(num[mid]<key):
            beg = mid+1
        elif(num[mid]>key):
            end = mid+1
        else:
            return mid
    return -1

print("Enter elements in sorted order: ")
try:
    nums =[]
    while True:
        nums.append(int(input()))
except:
    print(nums)

key = int(input("Enter key to search: "))

x = binary(nums,key)
if(x==-1):
    print("Given key is not found..")
else:
    print("Key",key,"is found at position: ",x)