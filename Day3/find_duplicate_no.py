def duplicate(arr):
    sum = 0
    for i in arr:
        sum += i
    n = len(arr)
    print(n-((n*(n+1)/2)-sum))
    
duplicate([1, 3, 4, 2, 2])
duplicate([3, 1, 3, 4, 2])
duplicate([1, 1])
duplicate([1, 4, 4, 2, 3])
list = list(range(1,1000000))
list.append(50000)
duplicate(list)