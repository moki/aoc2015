def part_1(input):
    floor = 0

    for c in input:
        floor += 1 if c == '(' else -1 if c == ')' else 0

    return floor

def part_2(input):
    counter = 0
    floor = 0

    for c in input:
        counter = counter + 1

        floor += 1 if c == '(' else -1 if c == ')' else 0

        if floor == -1:
            break

    return counter
