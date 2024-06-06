def selection(lst):
    n = len(lst)
    for i in range(n):
        mini = i
        for j in range(n):
            if lst[j] > lst[mini]:
                mini = j
            lst[mini],lst[i] = lst[i],lst[mini]
    return lst
lst = [56,4,23,87,3238,8623,953,3,68]
ans =selection(lst)
print(ans)