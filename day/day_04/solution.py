from hashlib import md5
from itertools import count

def part_1(input, zeroes = 5):
    input = input.strip()
    target = "0" * zeroes

    for i in count(0):
        s = input + str(i)

        hash = md5(s.encode("utf-8")).hexdigest()

        if hash[0:zeroes] == target:
            return i

    return 0

def part_2(input):
    return part_1(input, 6)
