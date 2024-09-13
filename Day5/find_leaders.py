def leaders(arr):
    n = len(arr)
    max = arr[n-1]
    leaders=[]
    leaders.append(max)
    for i in range(n-1,-1,-1):
        if max < arr[i]:
            max = arr[i]
            leaders.append(max)
    leaders.reverse()
    print(leaders)

leaders([16, 17, 4, 3, 5, 2])
leaders([1, 2, 3, 4, 0])
leaders([7, 10, 4, 10, 6, 5, 2])
leaders([100, 50, 20, 10])
list = list(range(1,1000001))
leaders(list)