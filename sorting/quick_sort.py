def sort(array):
    less =[]
    grater= []
    equal =[]
    if len(array)>1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(pivot)
            elif x > pivot:
                grater.append(x)
        return sort(less)+sort(equal)+sort(grater)
    else:
        return array
lst = [9,6,423,4,63,25]
ans =  sort(lst)
print(ans)