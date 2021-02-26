def _hash(x, y):
    return hash(str(x) + str(y))

def part_1(input):
    x, y = 0, 0

    counter = 0

    move_map = {
        "^": (0,1),
        ">": (1,0),
        "<": (-1,0),
        "v": (0,-1)
    }

    house_map = dict()

    house_map[_hash(x, y)] = 1

    for c in input:
        _x, _y = move_map.get(c, (0, 0))

        x += _x
        y += _y

        e = house_map.get(_hash(x,y))

        house_map[_hash(x,y)] = 1 if e == None else e + 1

    for k, v in house_map.items():
        counter += 1 if v > 0 else 0

    return counter

def part_2(input):
    return
