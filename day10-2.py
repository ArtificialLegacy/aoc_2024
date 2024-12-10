def solve(input: str):
    lines = input.split("\n")[:-1]
    assert len(lines) > 0

    map: list[list[tuple[int, int]]] = []
    trailheads: list[tuple[int, int]] = []

    for row in range(len(lines)):
        rowdata = lines[row]
        map.append([])
        for col in range(len(rowdata)):
            coldata = int(rowdata[col])

            if coldata == 9:
                map[row].append((coldata, 1))
            else:
                map[row].append((coldata, 0))

            if coldata == 0:
                trailheads.append((row, col))

    sum = 0

    for th in trailheads:
        sum += walk(map, th[0], th[1], 0)

    return sum


def walk(map: list[list[tuple[int, int]]], row: int, col: int, dir: int):
    current = map[row][col]

    found = 0

    if dir != 3 and row > 0:
        up = map[row - 1][col]
        if up[0] == current[0] + 1:
            if up[1] > 0:
                found += up[1]
            else:
                found += walk(map, row - 1, col, 1)

    if dir != 1 and row < len(map) - 1:
        down = map[row + 1][col]
        if down[0] == current[0] + 1:
            if down[1] > 0:
                found += down[1]
            else:
                found += walk(map, row + 1, col, 3)

    if dir != 2 and col > 0:
        left = map[row][col - 1]
        if left[0] == current[0] + 1:
            if left[1] > 0:
                found += left[1]
            else:
                found += walk(map, row, col - 1, 4)

    if dir != 4 and col < len(map[row]) - 1:
        right = map[row][col + 1]
        if right[0] == current[0] + 1:
            if right[1] > 0:
                found += right[1]
            else:
                found += walk(map, row, col + 1, 2)

    map[row][col] = (current[0], found)

    return found
