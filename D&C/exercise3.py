import unittest


def _integer_square_root(n, start, end):
    if start > end:
        return -1
        
    mid = (start + end) // 2
    
    if (mid ** 2 == n):
        return mid 
        
    if (mid ** 2 > n):
        if (mid - 1 > 0 and (mid - 1)**2 < n):
            return mid - 1
        return _integer_square_root(n, start, mid)
        
    return _integer_square_root(n, mid+1, end)

def integer_square_root(n):
    return _integer_square_root(n, 0, n)
    


class TestIntegerSquareRoot(unittest.TestCase):

    def test(self):
        self.assertEqual(integer_square_root(25), 5)
        self.assertEqual(integer_square_root(10), 3)
        self.assertEqual(integer_square_root(17), 4)
        self.assertEqual(integer_square_root(1), 1)
        self.assertEqual(integer_square_root(0), 0)

if __name__ == '__main__':
    unittest.main()
