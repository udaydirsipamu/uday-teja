def binary_search(arr,key):
    start,end=0,len(arr)-1
    while start<=end:
        mid=(start+end)//2
        if arr[mid]==key:
            return mid
        elif arr[mid]<key:
            srart=mid+1
        else:
            end=mid-1
    return -1
arr=list(map(int,input("Enter array elements").split()))
key=int(input("Enter element  to search:"))
print("Element found at position:",binary_search(arr,key))
        