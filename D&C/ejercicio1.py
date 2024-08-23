def _find_out_of_place(arr, low, high):
    if low == high:
        return 0
    
    mid = (low + high) // 2

    left = _find_out_of_place(arr, low, mid)
    rigth = _find_out_of_place(arr, mid + 1, high)

    #print(arr[low], ">", arr[mid+1], "and", arr[mid], ">",arr[mid+1], "and", arr[high], ">", arr[mid+1])
    #low izq inicio
    #mid izq final
    #mid+1 der inicio
    #high der final
    # izq_inicio > der_inicio y izq_final > der_inicio y der_final > izq_final
    if (arr[low] > arr[mid+1] and arr[mid] > arr[mid+1] and arr[high] > arr[mid]):
        return left + rigth + arr[mid+1]
    if (arr[low] > arr[mid+1] and arr[mid] > arr[mid+1] and arr[high] < arr[mid]):
        return left + rigth + arr[mid]
    
    if (arr[mid] > arr[mid+1]):
        return left + rigth + arr[mid]

    return left + rigth

def find_out_of_place(arr):
    start = 0
    end = len(arr) - 1
    if (arr[start] > arr[start+1]):
        return arr[start]
    if (arr[end] < arr[end-1] and len(arr) > 2):
        return arr[end]
    return _find_out_of_place(arr, start, end)


arr = [17, 19, 7, 20] 
print(f"Element out of place: 7 vs {find_out_of_place(arr)}")

arr = [19, 7, 20]
print(f"Element out of place: 19 vs {find_out_of_place(arr)}")

arr = [20, 1]
print(f"Element out of place: 20 vs {find_out_of_place(arr)}")

arr = [20, 25, 1]
print(f"Element out of place: 1 vs {find_out_of_place(arr)}")

arr = [20, 25, 1, 26]
print(f"Element out of place: 1 vs {find_out_of_place(arr)}")

arr = [6, 1, 9, 10, 12, 13, 14, 15]
print(f"Element out of place: 6 vs {find_out_of_place(arr)}")

arr = [2, 3, 15, 16, 19, 33, 4, 35]
print(f"Element out of place: 4 vs {find_out_of_place(arr)}")

arr = [1, 2, 3, 15, 11]
print(f"Element out of place: 15(It's okay if the result is 11) vs {find_out_of_place(arr)}")

arr = [111, 2, 3, 10, 11]
print(f"Element out of place: 111 vs {find_out_of_place(arr)}")


arr = [1,99, 3, 11]
print(f"Element out of place: 99 vs {find_out_of_place(arr)}")

