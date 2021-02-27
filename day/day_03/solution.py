def _hash(x, y):
    return hash(str(x) + "," + str(y))


def part_1(input):
    x, y = 0, 0

    move_map = {"^": (0, 1), ">": (1, 0), "<": (-1, 0), "v": (0, -1)}

    house_map = dict()

    house_map[_hash(x, y)] = 1

    for c in input:
        _x, _y = move_map.get(c, (0, 0))

        x += _x
        y += _y

        house_map[_hash(x, y)] = 1

    return len(house_map)


def part_2(input):
    hx, hy = 0, 0
    rx, ry = 0, 0

    move_map = {"^": (0, 1), ">": (1, 0), "<": (-1, 0), "v": (0, -1)}

    house_map = dict()

    house_map[_hash(0, 0)] = 1

    i = 0

    for c in input:
        _x, _y = move_map.get(c, (0, 0))

        if i % 2 == 0:
            _x += hx
            _y += hy

            hx = _x
            hy = _y
        else:
            _x += rx
            _y += ry

            rx = _x
            ry = _y

        house_map[_hash(_x, _y)] = 1

        i = i + 1

    return len(house_map)
