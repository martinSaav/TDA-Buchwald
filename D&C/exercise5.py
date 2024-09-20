import unittest


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    rigth = merge_sort(arr[mid:])
    
    return merge(left, rigth)

def merge(left, rigth):
    i = j = 0
    result = []

    while (i < len(left) and j < len(rigth)):
        if (left[i] > rigth[j]):
            result.append(rigth[j])
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
    
    return result


class MerseSortTest(unittest.TestCase):

    def test(self):
        self.assertEqual(merge_sort([]), [])
        self.assertEqual(merge_sort([1]), [1])
        self.assertEqual(merge_sort([1, 2]), [1, 2])
        self.assertEqual(merge_sort([2, 1]), [1, 2])
        self.assertEqual(merge_sort([2, 3, 1]), [1, 2, 3])
        self.assertEqual(merge_sort([3, 2, 1]), [1, 2, 3])
        self.assertEqual(merge_sort([99, 2, 33, 1, -3]), [-3, 1, 2, 33, 99])



if __name__ == '__main__':
    unittest.main()