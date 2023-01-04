import unittest
import week23 as f


class TestResults(unittest.TestCase):
    def test_factorization(self):
        ans = f.factorization(48)
        self.assertEqual(ans, [2, 2, 2, 2, 3])

    def test_gcd(self):
        ans = f.gcd(f.factorization(48), f.factorization(180))
        self.assertEqual(ans, 12)

    def test_lcm(self):
        ans = f.lcm(48, 180)
        self.assertEqual(ans, 720)


if __name__ == '__main__':
    unittest.main()
