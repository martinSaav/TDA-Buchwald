def merge_sort_count(arr):
    if len(arr) <= 1:
        return (0, arr)
    
    mid = len(arr) // 2

    (ra, left) = merge_sort_count(arr[:mid])
    (rb, rigth) = merge_sort_count(arr[mid:])
    
    (r, arr) = merge_count(left, rigth)

    return (r + ra + rb, arr)

def merge_count(left, rigth):
    i = j = inv =0
    result = []
    print(left, rigth)
    while (i < len(left) and j < len(rigth)):
        if (left[i] > rigth[j]):
            result.append(rigth[j])
            inv += (len(left) - i)
            j+=1
        else:
            result.append(left[i])
            i+=1


    while(i < len(left)):
        result.append(left[i])
        i+=1
    while(j < len(rigth)):
        result.append(rigth[j])
        j+=1
    return (inv, result)


def main():
    print(merge_sort_count([7,3,5,2,1,8,4,6]))

if __name__ == '__main__':
    main()
