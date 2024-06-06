def quick_sort(left,right,arr):
    if left<right:
        parti_pos = partision(left,right,arr)
        quick_sort(parti_pos+1,right,arr)
        quick_sort(left,parti_pos-1,arr)
    return arr
def partision(left,right,arr):
    i = left
    j = right-1
    pivot = arr[right]
    while i<j:
        # jab tak i ka index is less than last index and i element is less than pivot element
        # it means i wil increment till he finds element bigger than pivot elemet 
        while i < right and arr[i] < pivot:
            i+=1
            
            
        #  jab tak j ka index left index is aage hai aur j ka element pivot elment is bada hai
        #  it means j will decrement till he finds leeser element than pivot
        while j > left and arr[j] > pivot:
            j-=1
            
            
        #  unit increment karte karte agar i and cross each other 
        if i < j :
            arr[i],arr[j] = arr[j],arr[i]
            
    # when elemet at i index find greter than pivot 
    if arr[i]> pivot:
        arr[i],arr[right] = arr[right],arr[i]
    # it will return index at which [artision whill happen 
    return i
        
lst = [11,33,55,66,22,99,44]
ans = quick_sort(0,len(lst)-1,lst)
print(ans)
