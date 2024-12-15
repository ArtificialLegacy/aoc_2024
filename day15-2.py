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
            if coldata == "#":
                map[row].extend(["#", "#"])
            elif coldata == "O":
                map[row].extend(["[", "]"])
            elif coldata == ".":
                map[row].extend([".", "."])
            elif coldata == "@":
                map[row].extend(["@", "."])
                robot = (row, col * 2)

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
            if rowdata[col] == "[":
                sum += row * 100 + col

    return sum


def move(map: list[list[str]], pos: tuple[int, int], vec: tuple[int, int]):
    next = (pos[0] + vec[0], pos[1] + vec[1])
    nextc = map[next[0]][next[1]]

    if nextc == "#":
        return False

    if nextc in ["[", "]"]:
        if vec[0] != 0:
            c1 = check(map, (next[0], next[1]), vec)
            if not c1:
                return False

            d = 1
            if nextc == "]":
                d = -1

            c2 = check(map, (next[0], next[1] + d), vec)
            if not c2:
                return False

            if d == 1:
                d = 0

            move_box(map, (next[0], next[1] + d), vec)
        else:
            can = move(map, next, vec)
            if not can:
                return False

    map[next[0]][next[1]] = map[pos[0]][pos[1]]
    map[pos[0]][pos[1]] = "."

    return True


def move_box(map: list[list[str]], pos: tuple[int, int], vec: tuple[int, int]):
    next_left = (pos[0] + vec[0], pos[1] + vec[1])
    next_right = (pos[0] + vec[0], pos[1] + vec[1] + 1)

    next_leftc = map[next_left[0]][next_left[1]]
    next_rightc = map[next_right[0]][next_right[1]]

    if next_leftc == "[":
        move_box(map, next_left, vec)
    if next_leftc == "]":
        move_box(map, (next_left[0], next_left[1] - 1), vec)
    if next_rightc == "[":
        move_box(map, next_right, vec)

    map[next_left[0]][next_left[1]] = "["
    map[next_right[0]][next_right[1]] = "]"
    map[pos[0]][pos[1]] = "."
    map[pos[0]][pos[1] + 1] = "."


def check(map: list[list[str]], pos: tuple[int, int], vec: tuple[int, int]):
    next = (pos[0] + vec[0], pos[1] + vec[1])
    nextc = map[next[0]][next[1]]

    if nextc == "#":
        return False

    if nextc == "[":
        c1 = check(map, next, vec)
        if not c1:
            return False
        c2 = check(map, (next[0], next[1] + 1), vec)
        if not c2:
            return False
    if nextc == "]":
        c1 = check(map, next, vec)
        if not c1:
            return False
        c2 = check(map, (next[0], next[1] - 1), vec)
        if not c2:
            return False

    return True
