def selection_sort(arr):
    if(len(arr) < 2):
        return arr
    
    sorted_arr = []
    
    for idx in range(len(arr)):
        lower = find_smallest(arr)
        sorted_arr.append(arr.pop(lower))

    return sorted_arr

def find_smallest(arr):
    low_idx = 0
    low_value = arr[0]
    
    for i in range(len(arr)):
        if arr[i] < low_value:
            low_value = arr[i]
            low_idx = i
            
    return low_idx