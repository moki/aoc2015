M = 1000
N = 1000


def grid_pretty_print(grid):
    print()

    print("{: >3}".format(""), end="")
    for j, c in enumerate(grid[0]):
        print("{: >3}".format(j), end="")

    print("\n")

    for i, row in enumerate(grid):
        print("{: >3}".format(i), end="")

        for j, col in enumerate(row):
            print("{: >3}".format(col), end="")

        print("\n")


def grid_apply(grid, fn, x, y, _x, _y):
    for i in range(x, _x + 1):
        for j in range(y, _y + 1):
            grid[i][j] = fn(grid, i, j)


def grid_count_lights(grid):
    counter = 0

    for row in grid:
        for col in row:
            if col:
                counter += 1

    return counter


def grid_count_brightness(grid):
    counter = 0

    for row in grid:
        for col in row:
            if col:
                counter += col

    return counter


def part_1(input):
    grid = [[0 for j in range(M)] for i in range(N)]

    def toggle(grid, x, y):
        return 0 if grid[x][y] else 1

    def turn_on(grid, x, y):
        return 1

    def turn_off(grid, x, y):
        return 0

    def id(grid, x, y):
        return grid[x][y]

    for command in input.split("\n"):
        if not len(command):
            continue

        _command = command.strip().split()

        cmd_i = 0
        from_xy_i = 0
        to_xy_i = 0

        if len(_command) == 5:
            cmd_i = 1
            from_xy_i = 2
            to_xy_i = 4
        else:
            from_xy_i = 1
            to_xy_i = 3

        cmd = _command[cmd_i]
        from_x, from_y = _command[from_xy_i].split(",")
        to_x, to_y = _command[to_xy_i].split(",")

        fn = {"toggle": toggle, "on": turn_on, "off": turn_off}.get(cmd, id)

        grid_apply(grid, fn, int(from_x), int(from_y), int(to_x), int(to_y))

    return grid_count_lights(grid)


def part_2(input):
    grid = [[0 for j in range(M)] for i in range(N)]

    def toggle(grid, x, y):
        return grid[x][y] + 2

    def turn_on(grid, x, y):
        return grid[x][y] + 1

    def turn_off(grid, x, y):
        brightness = grid[x][y] - 1
        return brightness if brightness > 0 else 0

    def id(grid, x, y):
        return grid[x][y]

    for command in input.split("\n"):
        if not len(command):
            continue

        _command = command.strip().split()

        cmd_i = 0
        from_xy_i = 0
        to_xy_i = 0

        if len(_command) == 5:
            cmd_i = 1
            from_xy_i = 2
            to_xy_i = 4
        else:
            from_xy_i = 1
            to_xy_i = 3

        cmd = _command[cmd_i]
        from_x, from_y = _command[from_xy_i].split(",")
        to_x, to_y = _command[to_xy_i].split(",")

        fn = {"toggle": toggle, "on": turn_on, "off": turn_off}.get(cmd, id)

        grid_apply(grid, fn, int(from_x), int(from_y), int(to_x), int(to_y))

    return grid_count_brightness(grid)
