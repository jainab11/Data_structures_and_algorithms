def binary(arr,n):
    low = 0
    high = len(arr)-1
    # apply binary search
    while low <= high:
        # until low is less than ig low cross high there is no element
        # now find mid 
        mid = (low+high)//2
        if arr[mid]<n:
            low = mid+1
        elif arr[mid] > n:
            high = mid -1
        else :
            return mid
    return -1
lst = [1,2,3,4,5,6,7,8,9,10]
n =10
print(binary(lst ,n))