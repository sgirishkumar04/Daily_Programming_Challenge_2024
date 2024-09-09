def sort(arr):
    zero = 0
    one = 0
    two = 0
    for i in arr:
        if i == 0:
            zero+=1
        elif i == 1:
            one+=1
        elif i == 2:
            two+=1
        else:
            print("Invalid number!!")
    index = 0
    for i in range(zero):
        arr[index] = 0
        index+=1

    for i in range(one):
        arr[index] = 1
        index+=1

    for i in range(two):
        arr[index] = 2
        index+=1
    print(arr)

sort([0, 1, 2, 1, 0, 2, 1, 0])
sort([2, 2, 2, 2])
sort([0, 0, 0, 0])
sort([1, 1, 1, 1])
sort([2, 0, 1])
sort([])