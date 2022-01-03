import unittest

from main import *


class TestBoyerMoore(unittest.TestCase):

    def setUp(self):
        self.input_adjacency_matrix = [[0, 16, 13, 0, 0, 0],
                    [0, 0, 10, 12, 0, 0],
                    [0, 4, 0, 0, 14, 0],
                    [0, 0, 9, 0, 0, 20],
                    [0, 0, 0, 7, 0, 4],
                    [0, 0, 0, 0, 0, 0]]
        self.source = 0
        self.sink = 5
        self.output = [[1, 3], [4, 3], [4, 5]]

    def testBoyerMoore(self):
        self.assertEqual(count_min_cut(self.input_adjacency_matrix, self.source, self.sink), self.output)


if __name__ == "__main__":
    unittest.main()
