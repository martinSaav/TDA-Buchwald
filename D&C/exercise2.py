def _unit_test(arr, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2

    if (arr[mid] == 0):
        if(mid - 1 > 0 and arr[mid-1] == 1):
            return mid
        if (mid - 1 < 0):
            return 0
        return _unit_test(arr, low, mid)
    
    if (mid + 1 < high and arr[mid+1] == 0):
        return mid + 1

    return _unit_test(arr, mid+1, high)

def unit_test(arr):
    return _unit_test(arr, 0, len(arr)-1)



arr = [1, 1, 0, 0, 0] 
print(unit_test(arr))

arr = [0, 0, 0, 0, 0]
print(unit_test(arr))

arr = [1, 1, 1, 1, 1]
print(unit_test(arr))
