def linear_search(arr,key):
    for i in range(len(arr)):
        if arr[i]==key:
            return i
    return -1
arr=list(map(int,input("Enter array elements").split()))
key=int(input("Enter element  to search:"))
print("Element found at position:",linear_search(arr,key))
         