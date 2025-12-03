def array_len(idx, arr):
    try:
        arr[idx] 
    except IndexError:
        return 0
    return 1 + array_len(idx + 1, arr)

def array_len_v2(arr):
    if arr == []:
        return 0
    return 1 + array_len_v2(arr[1:])
    