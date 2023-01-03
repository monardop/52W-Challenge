import unittest
import week23 as f


class TestResults(unittest.TestCase):
    def test1(self):
        print("Testing factorization")
        ans = f.factorization(48)
        self.assertEqual(ans, [2, 2, 2, 2, 3])

    def test2(self):
        print("Testing gcd")
        ans = f.gcd(f.factorization(48), f.factorization(180))
        self.assertEqual(ans, 12)

    def test3(self):
        print("Testing lcm")
        ans = f.lcm(48, 180)
        self.assertEqual(ans, 720)


if __name__ == '__main__':
    unittest.main()
