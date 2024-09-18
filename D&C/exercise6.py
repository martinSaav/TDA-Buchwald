import unittest

def karatsuba(x, y):
    if x < 10 or y < 10:
        return x * y

    n = max(len(str(x)), len(str(y)))
    half = n // 2

    x1, x0 = divmod(x, 10**half)
    y1, y0 = divmod(y, 10**half)

    p = karatsuba(x0 + x1, y0 + y1)
    x0y0 = karatsuba(x0, y0)
    x1y1 = karatsuba(x1, y1)

    return (x1y1 * 10**(2*half)) + ((p - x1y1 - x0y0) * 10**half) + x0y0

class KaratsubaTest(unittest.TestCase):

    def test(self):
        self.assertEqual(karatsuba(1234, 5678), 7006652)
        self.assertEqual(karatsuba(10000, 10000), 100000000)



if __name__ == '__main__':
    unittest.main()
