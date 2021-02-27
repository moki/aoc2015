from functools import reduce


def part_1(input):
    lines = input.split("\n")
    paper = 0

    for line in lines:
        if len(line) == 0:
            continue

        ds = list(map(lambda d: int(d), line.split("x")))

        sides = [ds[0] * ds[1], ds[1] * ds[2], ds[0] * ds[2]]

        m = reduce(lambda a, b: min(a, b), sides, sides[0])

        paper += reduce(lambda a, b: a + b * 2, sides, 0) + m

    return paper


def part_2(input):
    lines = input.split("\n")
    ribbon = 0

    for line in lines:
        if len(line) == 0:
            continue

        ds = list(map(lambda d: int(d), line.split("x")))

        bow = reduce(lambda a, b: a * b, ds, 1)

        print(bow)

        ribbon += bow

        m = reduce(lambda a, b: min(a, b), ds, ds[0])

        ds.remove(m)

        m2 = reduce(lambda a, b: min(a, b), ds, ds[0])

        ribbon += m2 + m2 + m + m

    return ribbon
