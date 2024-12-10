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

            map[row].append((coldata, 0))
            if coldata == 0:
                trailheads.append((row, col))

    sum = 0

    idx = 1
    for th in trailheads:
        sum += walk(map, th[0], th[1], 0, idx)
        idx += 1

    return sum


def walk(map: list[list[tuple[int, int]]], row: int, col: int, dir: int, th: int):
    current = map[row][col]

    if current[0] == 9 and current[1] != th:
        map[row][col] = (9, th)
        return 1

    found = 0

    if dir != 3 and row > 0:
        up = map[row - 1][col]
        if up[1] != th and up[0] == current[0] + 1:
            found += walk(map, row - 1, col, 1, th)

    if dir != 1 and row < len(map) - 1:
        down = map[row + 1][col]
        if down[1] != th and down[0] == current[0] + 1:
            found += walk(map, row + 1, col, 3, th)

    if dir != 2 and col > 0:
        left = map[row][col - 1]
        if left[1] != th and left[0] == current[0] + 1:
            found += walk(map, row, col - 1, 4, th)

    if dir != 4 and col < len(map[row]) - 1:
        right = map[row][col + 1]
        if right[1] != th and right[0] == current[0] + 1:
            found += walk(map, row, col + 1, 2, th)

    map[row][col] = (current[0], th)

    return found
