def array_sum(arr):
    if len(arr) == 0:
        return 0
    elif len(arr) < 2:
        return arr[0]
    return arr[0] + array_sum(arr[1:])