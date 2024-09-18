def _max_crossing_subarray(arr, left, mid, right):
    # Suma máxima del subarreglo que cruza la mitad hacia la izquierda
    left_sum = float('-inf')
    total = 0
    max_left = mid
    for i in range(mid, left - 1, -1):
        total += arr[i]
        if total > left_sum:
            left_sum = total
            max_left = i

    # Suma máxima del subarreglo que cruza la mitad hacia la derecha
    right_sum = float('-inf')
    total = 0
    max_right = mid + 1
    for i in range(mid + 1, right + 1):
        total += arr[i]
        if total > right_sum:
            right_sum = total
            max_right = i

    # Devolver la suma máxima cruzando la mitad y los índices
    return left_sum + right_sum, max_left, max_right

def _max_subarray(arr, left, right):
    if left == right:  # Caso base: un solo elemento
        return arr[left], left, right

    # Calcular el punto medio
    mid = (left + right) // 2

    # Recursión sobre la mitad izquierda y derecha, y el subarreglo cruzando la mitad
    left_max, left_start, left_end = _max_subarray(arr, left, mid)
    right_max, right_start, right_end = _max_subarray(arr, mid + 1, right)
    cross_max, cross_start, cross_end = _max_crossing_subarray(arr, left, mid, right)

    # Devolver el máximo de los tres junto con los índices correspondientes
    if left_max >= right_max and left_max >= cross_max:
        return left_max, left_start, left_end
    elif right_max >= left_max and right_max >= cross_max:
        return right_max, right_start, right_end
    return cross_max, cross_start, cross_end

# Función principal
def max_subarray(arr):
    max_sum, start, end = _max_subarray(arr, 0, len(arr) - 1)
    return arr[start:end + 1]