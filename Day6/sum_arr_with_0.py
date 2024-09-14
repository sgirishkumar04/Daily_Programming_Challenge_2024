def zero_sum(arr):
    sum_map = {}
    sum = 0
    result = []
    
    for i in range(len(arr)):
        sum += arr[i]
        
        if sum == 0:
            result.append((0, i))
        
        if sum in sum_map:
            start_indices = sum_map[sum]
            for start_index in start_indices:
                result.append((start_index + 1, i))
        
        if sum in sum_map:
            sum_map[sum].append(i)
        else:
            sum_map[sum] = [i]
    
    return result
print(zero_sum([1, 2, -3, 3, -1, 2]))
print(zero_sum([4, -1, -3, 1, 2, -1]))
print(zero_sum([0, 0, 0]))
print(zero_sum([-3, 1, 2, -3, 4, 0]))