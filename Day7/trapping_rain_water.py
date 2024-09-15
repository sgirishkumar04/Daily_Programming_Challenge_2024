from collections import defaultdict

def water(arr):
    a=defaultdict(list)
    max=0
    for i in range(len(arr)-2):
        if arr[max]<arr[i]:
            max=i
        a[i+1].append(max)
    maxii=len(arr)-1
    for i in range(len(arr)-1,1,-1):
        if arr[maxii]<arr[i]:
            maxii=i
        a[i-1].append(maxii)
    sum=0
    for i in a:
        k=min(arr[a[i][0]],arr[a[i][1]])
        
        if arr[i]<k:
            sum+=(k-arr[i])
            
    return sum
print(water([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
print(water([4, 2, 0, 3, 2, 5]))
print(water( [1, 1, 1]))
print(water([5]))
print(water([2, 0, 2]))
