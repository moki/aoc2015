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

        print("\n")
        print("input")
        print(input)
        print("output")
        print(output)

    def test_part_2(self):
        inputs = [")", "()())"]
        outputs = [1, 5]

        cases = zip(inputs, outputs)

        for case in cases:
            self.assertEqual(part_2(case[0]), case[1])

        if not INPUT:
            return

        input = read_input("day/day_01/input/part_2")
        output = part_2(input)

        print("\n")
        print("input")
        print(input)
        print("output")
        print(output)
