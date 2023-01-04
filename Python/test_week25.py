import unittest
import week25 as f


class MyTestCase(unittest.TestCase):
    def test_winnerP1(self):
        msg = f.win_check('R', 'S')
        self.assertEqual(msg, 'Player 1 wins')

    def test_winnerP2(self):
        msg = f.win_check('R', 'P')
        self.assertEqual(msg, 'Player 2 wins')

    def test_draw(self):
        msg = f.win_check('R', 'R')
        self.assertEqual(msg, 'Tie')


if __name__ == '__main__':
    unittest.main()
