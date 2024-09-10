def missing(arr):
    sum = 0
    for i in arr:
        sum += i
    n = len(arr)+1
    print((n*(n+1)/2)-sum)

missing([1, 2, 4, 5])
missing([2, 3, 4, 5])
missing([1, 2, 3, 4])
missing([1])
missing(list(range(1,1000000)))