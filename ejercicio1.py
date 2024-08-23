def _find_out_of_place(arr, low, high):
    # Caso base: si solo hay un elemento o dos en la sublista
    if low == high:
        return 0
    
    # Encuentra el punto medio
    mid = (low + high) // 2

    izq = _find_out_of_place(arr, low, mid)
    der = _find_out_of_place(arr, mid + 1, high)

    #print(arr[low], ">", arr[mid+1], "and", arr[mid], ">",arr[mid+1], "and", arr[high], ">", arr[mid+1])
    #low izq inicio
    #mid izq final
    #mid+1 der inicio
    #high der final
    # izq_inicio > der_inicio y izq_final > der_inicio y der_final > izq_final
    if (arr[low] > arr[mid+1] and arr[mid] > arr[mid+1] and arr[high] > arr[mid]):
        return izq + der + arr[mid+1]
    if (arr[low] > arr[mid+1] and arr[mid] > arr[mid+1] and arr[high] < arr[mid]):
        return izq + der + arr[mid]
    
    if (arr[mid] > arr[mid+1]):
        return izq + der + arr[mid]


    return izq + der

def find_out_of_place(arr):
    start = 0
    end = len(arr) - 1
    if (arr[start] > arr[start+1]):
        return arr[start]
    if (arr[end] < arr[end-1] and len(arr) > 2):
        return arr[end]
    return _find_out_of_place(arr, start, end)

# Ejemplo de uso
arr = [17, 19, 7, 20] 
print(f"Elemento fuera de lugar: 7 vs {find_out_of_place(arr)}")

arr = [19, 7, 20]
print(f"Elemento fuera de lugar: 19 vs {find_out_of_place(arr)}")

arr = [20, 1]
print(f"Elemento fuera de lugar: 20 vs {find_out_of_place(arr)}")

arr = [20, 25, 1]
print(f"Elemento fuera de lugar: 1 vs {find_out_of_place(arr)}")

arr = [20, 25, 1, 26]
print(f"Elemento fuera de lugar: 1 vs {find_out_of_place(arr)}")

arr = [6, 1, 9, 10, 12, 13, 14, 15]
print(f"Elemento fuera de lugar: 6 vs {find_out_of_place(arr)}")

arr = [2, 3, 15, 16, 19, 33, 4, 35]
print(f"Elemento fuera de lugar: 4 vs {find_out_of_place(arr)}")

arr = [1, 2, 3, 15, 11]
print(f"Elemento fuera de lugar: 15(sirve igual si da 11 pero bueno) vs {find_out_of_place(arr)}")

arr = [111, 2, 3, 10, 11]
print(f"Elemento fuera de lugar: 111 vs {find_out_of_place(arr)}")


arr = [1,99, 3, 11]
print(f"Elemento fuera de lugar: 99 vs {find_out_of_place(arr)}")

