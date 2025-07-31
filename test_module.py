import unittest
from RPS_game import play, quincy, abbey, kris, mr_x
from RPS import player

class UnitTests(unittest.TestCase):
    def test_quincy(self):
        result = play(player, quincy, 1000)
        self.assertGreater(result[0], result[1])

    def test_abbey(self):
        result = play(player, abbey, 1000)
        self.assertGreater(result[0], result[1])

    def test_kris(self):
        result = play(player, kris, 1000)
        self.assertGreater(result[0], result[1])

    def test_mr_x(self):
        result = play(player, mr_x, 1000)
        self.assertGreater(result[0], result[1])

if __name__ == "__main__":
    unittest.main()
