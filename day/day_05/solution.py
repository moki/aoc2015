def count_vowel(line):
    return len([c for c in line if c in "aeiou"])

def is_vowelly(line):
    return count_vowel(line) > 2

def is_doublly(line):
    return len([line[i] for i in range(len(line) - 1) if line[i] == line[i+1]])

def is_valid(line):
    return not sum(c in line for c in ['ab', 'cd', 'pq', 'xy'])

def part_1(input):
    return len([ line for line in input.split("\n") if is_vowelly(line) and is_doublly(line) and is_valid(line) ])

def part_2(input):
    lines = input.split("\n")

    counter = 0

    for line in lines:
        cond_1 = False

        for i in range(len(line) - 2):
            for j in range(i + 2, len(line) - 1):
                if line[i] == line[j] and line[i+1] == line[j+1]:
                    cond_1 = True
                    break

        cond_2 = False

        for i in range(1, len(line) - 1):
            if line[i-1] == line[i+1]:
                cond_2 = True
                break

        if cond_1 and cond_2:
            counter = counter + 1

    return counter
