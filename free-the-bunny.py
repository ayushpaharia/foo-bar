import itertools
import unittest


class TestDodgeTheLasers(unittest.TestCase):
    def test_1(self):
        num_buns = 2
        num_required = 1
        self.assertEqual(answer(num_buns, num_required), [[0], [0]])

    def test_2(self):
        num_buns = 5
        num_required = 3
        self.assertEqual(answer(num_buns, num_required), [[0, 1, 2, 3, 4, 5], [0, 1, 2, 6, 7, 8], [0, 3, 4, 6, 7, 9],
                                                          [1, 3, 5, 6, 8, 9], [2, 4, 5, 7, 8, 9]])

    def test_torture(self):
        num_buns = 4
        num_required = 4
        self.assertEqual(answer(num_buns, num_required), [[0], [1], [2], [3]])


def answer(num_buns, num_required):

    num_instance = num_buns - num_required + 1
    key_locations = list(itertools.combinations(range(num_buns),
                                                num_instance))
    key_lists = [[] for i in range(num_buns)]
    for key, locs in enumerate(key_locations):
        for loc in locs:
            key_lists[loc].append(key)

    return key_lists


if __name__ == '__main__':
    unittest.main()
