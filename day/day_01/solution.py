def part_1(input):
    floor = 0

    for c in input:
        floor += 1 if c == '(' else -1 if c == ')' else 0

    return floor

def part_2(input):
    print(input)
    return "solution_2"
