def merge(arr):
    #  first base case for recursion
    if len(arr)<= 1:
        return
    mid = len(arr)//2
    left_arr = arr[:mid] # goes from start to middle of arr
    right_arr =arr[mid:]# goes from middle part of arr to end
    # recursion
    merge(left_arr)
    merge(right_arr)
    
    # merge code
    i = 0 # left_arr  index
    j = 0 # right_arr index
    k = 0 # merge arr index
    # this loop will run till till index is less than left and right len
    while i<len(left_arr) and j< len(right_arr):
        if left_arr[i] < right_arr[j]:
            arr[k] = left_arr[i]
            i+=1
            
        else:
            arr[k] = right_arr[j]
            j+=1
        k+=1
    # suppose right elemtnt and left still have some element
    while i <len(left_arr):
        arr[k] = left_arr[i]
        i+=1
        k+=1
    while j< len(right_arr) :
        arr[k] = right_arr[j]
        j+=1
        k+=1
# return ar
    
            
            
lst = [33,11,99,22,44,66,88,55]
merge(lst)
print(lst)