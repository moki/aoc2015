import unittest
import os

from day.day_01.solution import part_1, part_2

INPUT = os.environ["INPUT"]

def read_input(path):
    with open(path, "r") as f:
        return f.read()

class day_01_test(unittest.TestCase):
    def test_part_1(self):
        inputs = ["()()", "(()(()(", "))(((((", "))(", ")())())"]
        outputs = [0, 3, 3, -1, -3]

        cases = zip(inputs, outputs)

        for case in cases:
            self.assertEqual(part_1(case[0]), case[1])

        if not INPUT:
            return

        input = read_input("day/day_01/input/part_1")
        output = part_1(input)
        print("\npart_1 input:\n")
        print("\n", input, "\n")
        print("\noutput:\n")
        print("\n", output, "\n")

    def test_part_2(self):
        if not INPUT:
            return

        input = read_input("day/day_01/input/part_2")

        r = part_2(input)

        self.assertEqual(r, "solution_2")
