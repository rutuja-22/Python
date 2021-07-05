def bsort(arr):
    for i in range(len(arr)-1,0,-1):
        for j in range(i):
            '''temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp'''
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1]= arr[j+1],arr[j]
    return arr

arr = [24,67,23,89,45,90]
arr1 = bsort(arr)
print(arr1)
