def merge(arr1, arr2):
    n = len(arr1)
    m = len(arr2)
    i, j = m - 1, 0

    while i >= 0 and j < n:
        if arr1[i] > arr2[j]:
            arr1[i], arr2[j] = arr2[j], arr1[i]
        i -= 1
        j += 1

    arr1.sort()
    arr2.sort()
    print(arr1)
    print(arr2)

print("Test 1")
merge([1, 3, 5], [2, 4, 6])
print("Test 2")
merge([10, 12, 14],[1, 3, 5])
print("Test 3")
merge([2, 3, 8],[4, 6, 10])
print("Test 4")
merge([1],[2])

