from hashlib import md5
from itertools import count

def part_1(input):
    input = input.strip()

    for i in count(0):
        s = input + str(i)

        hash = md5(s.encode("utf-8")).hexdigest()

        if hash[0:5] == "00000":
            return i

    return 0

def part_2(input):
    return len(input)
