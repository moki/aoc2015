import unittest
import os

from day.day_01.solution import part_1 as day_1_part_1, part_2 as day_1_part_2
from day.day_02.solution import part_1 as day_2_part_1, part_2 as day_2_part_2

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
            self.assertEqual(day_1_part_1(case[0]), case[1])

        if not INPUT:
            return

        input = read_input("day/day_01/input/part_1")
        output = day_1_part_1(input)

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
            self.assertEqual(day_1_part_2(case[0]), case[1])

        if not INPUT:
            return

        input = read_input("day/day_01/input/part_2")
        output = day_1_part_2(input)

        print("\n")
        print("input")
        print(input)
        print("output")
        print(output)

class day_02_test(unittest.TestCase):
    def test_part_1(self):
        inputs = ["2x3x4", "1x1x10"]
        outputs = [58, 43]

        cases = zip(inputs, outputs)

        for case in cases:
            self.assertEqual(day_2_part_1(case[0]), case[1])

        if not INPUT:
            return

        input = read_input("day/day_02/input/part_1")
        output = day_2_part_1(input)

        print("\n")
        print("input")
        print(input)
        print("output")
        print(output)

    def test_part_2(self):
        inputs = ["2x3x4", "1x1x10"]
        outputs = [34, 14]

        cases = zip(inputs, outputs)

        for case in cases:
            self.assertEqual(day_2_part_2(case[0]), case[1])

        if not INPUT:
            return

        input = read_input("day/day_02/input/part_2")
        output = day_2_part_2(input)

        print("\n")
        print("input")
        print(input)
        print("output")
        print(output)
