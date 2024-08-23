import unittest


def _peak_position(arr, start, end):
    if start >= end:
        return -1
    
    mid = (start + end) // 2

    if arr[mid-1] < arr[mid] > arr[mid+1]:
        return mid
    
    if arr[mid-1] > arr[mid]:
        return _peak_position(arr, start, mid)
    
    return _peak_position(arr, mid + 1, end)

def peak_position(arr):
    return _peak_position(arr, 0, len(arr)-1)


class TestPeakPosition(unittest.TestCase):

    def test(self):
        self.assertEqual(peak_position([1, 5, 0]), 1)
        self.assertEqual(peak_position([1, 2, 3, 1, 0, -2]), 2)
        self.assertEqual(peak_position([1, 2, 3, 1, 0, -2, -3, -5, -10, -20]), 2)
        self.assertEqual(peak_position([1, 2, 3, 6, 7, 8, 9, 20, 21, -1, -3]), 8)


if __name__ == '__main__':
    unittest.main()