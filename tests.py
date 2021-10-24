import unittest
from ticktackgame import TicTacGame, validate_answer, validate_name

class TestTicTacGame(unittest.TestCase):
    def setUp(self):
        self.game = TicTacGame()

    def test_winner_at_start(self):
        self.assertFalse(self.game.check_winner())

    def test_count_moves_at_start(self):
        self.assertEqual(self.game.count, 0)

    def test_name_invalid(self):
        with self.assertRaises(ValueError):
            validate_name('12345')

    def test_name_valid(self):
        self.assertTrue(validate_name('Olya'))

    def test_answer_invalid(self):
        with self.assertRaises(ValueError):
            validate_answer('26')

    def test_answer_invalid_not_number(self):
        with self.assertRaises(ValueError):
            validate_answer('abc')

    def test_answer_valid(self):
        self.assertTrue(validate_answer('25'))

if __name__ == '__main__':
    unittest.main()