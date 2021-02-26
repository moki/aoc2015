import unittest
import os

from day.day_01.solution import part_1 as day_1_part_1, part_2 as day_1_part_2
from day.day_02.solution import part_1 as day_2_part_1, part_2 as day_2_part_2
from day.day_03.solution import part_1 as day_3_part_1, part_2 as day_3_part_2
from day.day_04.solution import part_1 as day_4_part_1, part_2 as day_4_part_2
from day.day_05.solution import part_1 as day_5_part_1, part_2 as day_5_part_2

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

class day_03_test(unittest.TestCase):
    def test_part_1(self):
        inputs = [">", "^>v<", "^v^v^v^v^v"]
        outputs = [2, 4, 2]

        cases = zip(inputs, outputs)

        for case in cases:
            self.assertEqual(day_3_part_1(case[0]), case[1])

        if not INPUT:
            return

        input = read_input("day/day_03/input/part_1")
        output = day_3_part_1(input)

        print("\n")
        print("input")
        print(input)
        print("output")
        print(output)

    def test_part_2(self):
        inputs = ["^>", "^>v<", "^v^v^v^v^v"]
        outputs = [3, 3, 11]

        cases = zip(inputs, outputs)

        for case in cases:
            self.assertEqual(day_3_part_2(case[0]), case[1])

        if not INPUT:
            return

        input = read_input("day/day_03/input/part_2")
        output = day_3_part_2(input)

        print("\n")
        print("input")
        print(input)
        print("output")
        print(output)

class day_04_test(unittest.TestCase):
    def test_part_1(self):
        inputs = ["abcdef", "pqrstuv"]
        outputs = [609043, 1048970]

        cases = zip(inputs, outputs)

        for case in cases:
            self.assertEqual(day_4_part_1(case[0]), case[1])

        if not INPUT:
            return

        input = read_input("day/day_04/input/part_1")
        output = day_4_part_1(input)

        print("\n")
        print("input")
        print(input)
        print("output")
        print(output)

    def test_part_2(self):
        if not INPUT:
            return

        input = read_input("day/day_04/input/part_1")
        output = day_4_part_2(input)

        print("\n")
        print("input")
        print(input)
        print("output")
        print(output)

class day_05_test(unittest.TestCase):
    def test_part_1(self):
        inputs = [
                "aeixx",
                "xazddegov",
                "aeddioullaeiouzzaeiou",
                "ugknbfddgicrmopn",
                "aaa",
                "haegwjzuvuyypxyu",
                "jchzalrnumimnmhp",
                "dvszwmarrgswjxmb"
        ]

        outputs = [
            1,
            1,
            1,
            1,
            1,
            0,
            0,
            0
        ]

        cases = zip(inputs, outputs)

        for case in cases:
            self.assertEqual(day_5_part_1(case[0]), case[1])

        if not INPUT:
            return

        input = read_input("day/day_05/input/part_1")
        output = day_5_part_1(input)

        print("\n")
        print("input")
        print(input)
        print("output")
        print(output)
