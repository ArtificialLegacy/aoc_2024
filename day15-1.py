def solve(input: str):
    content = input.split("\n\n")
    assert len(content) == 2

    map: list[list[str]] = []

    robot = (-1, -1)

    mapdata = content[0].split("\n")
    for row in range(len(mapdata)):
        rowdata = mapdata[row]
        map.append([])
        for col in range(len(rowdata)):
            coldata = rowdata[col]
            map[row].append(coldata)
            if coldata == "@":
                robot = (row, col)

    vecs = {"<": (0, -1), ">": (0, 1), "^": (-1, 0), "v": (1, 0)}

    for d in content[1]:
        if d == "\n":
            continue

        vec = vecs[d]
        can = move(map, robot, vec)
        if can:
            robot = (robot[0] + vec[0], robot[1] + vec[1])

    sum = 0

    for row in range(len(map)):
        rowdata = map[row]
        for col in range(len(rowdata)):
            if rowdata[col] == "O":
                sum += row * 100 + col

    return sum


def move(map: list[list[str]], pos: tuple[int, int], vec: tuple[int, int]):
    next = (pos[0] + vec[0], pos[1] + vec[1])

    if map[next[0]][next[1]] == "#":
        return False

    if map[next[0]][next[1]] == "O":
        can = move(map, next, vec)
        if not can:
            return False

    map[next[0]][next[1]] = map[pos[0]][pos[1]]
    map[pos[0]][pos[1]] = "."

    return True
