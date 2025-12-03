def highest(arr):
    def helper(idx, current):
        if idx == len(arr):
            return current
        
        if current is None or arr[idx] > current:
            return helper(idx + 1, arr[idx])
        
        return helper(idx + 1, current)

    return helper(0, None)