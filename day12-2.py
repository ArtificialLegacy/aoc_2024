def solve(input: str):
    content = input.split("\n")[:-1]
    assert len(content) > 0

    map: list[list[tuple[int, bool]]] = []

    map.append([(-1, True) for _ in range(len(content[0]) + 2)])

    for row in range(len(content)):
        rowdata = content[row]
        map.append([(-1, True)])

        for col in range(len(rowdata)):
            coldata = rowdata[col]
            map[row + 1].append((ord(coldata), False))

        map[row + 1].append((-1, True))

    map.append([x for x in map[0]])

    price = 0

    for row in range(len(map) - 2):
        for col in range(len(map[row + 1]) - 2):
            if not map[row + 1][col + 1][1]:
                d = count(map, row + 1, col + 1)
                price += d[0] * d[1]

    return price


def count(map: list[list[tuple[int, bool]]], row: int, col: int):
    area = 1
    points = 0

    value = map[row][col][0]

    map[row][col] = (value, True)

    tl = map[row - 1][col - 1]
    tc = map[row - 1][col]
    tr = map[row - 1][col + 1]
    ml = map[row][col - 1]
    mr = map[row][col + 1]
    bl = map[row + 1][col - 1]
    bc = map[row + 1][col]
    br = map[row + 1][col + 1]

    adj = 0

    if tc[0] == value:
        adj += 1
        if not map[row - 1][col][1]:
            d = count(map, row - 1, col)
            area += d[0]
            points += d[1]

    if ml[0] == value:
        adj += 1
        if not map[row][col - 1][1]:
            d = count(map, row, col - 1)
            area += d[0]
            points += d[1]

    if mr[0] == value:
        adj += 1
        if not map[row][col + 1][1]:
            d = count(map, row, col + 1)
            area += d[0]
            points += d[1]

    if bc[0] == value:
        adj += 1
        if not map[row + 1][col][1]:
            d = count(map, row + 1, col)
            area += d[0]
            points += d[1]

    if adj == 0:
        points += 4
    elif adj == 1:
        points += 2
    elif adj == 2:
        if tc[0] == value and mr[0] == value:
            points += 1
            if tr[0] != value:
                points += 1
        elif mr[0] == value and bc[0] == value:
            points += 1
            if br[0] != value:
                points += 1
        elif bc[0] == value and ml[0] == value:
            points += 1
            if bl[0] != value:
                points += 1
        elif ml[0] == value and tc[0] == value:
            points += 1
            if tl[0] != value:
                points += 1
    elif adj == 3:
        if tc[0] != value:
            if bl[0] != value:
                points += 1
            if br[0] != value:
                points += 1
        elif mr[0] != value:
            if tl[0] != value:
                points += 1
            if bl[0] != value:
                points += 1
        elif bc[0] != value:
            if tl[0] != value:
                points += 1
            if tr[0] != value:
                points += 1
        elif ml[0] != value:
            if tr[0] != value:
                points += 1
            if br[0] != value:
                points += 1
    elif adj == 4:
        if tl[0] != value:
            points += 1
        if tr[0] != value:
            points += 1
        if bl[0] != value:
            points += 1
        if br[0] != value:
            points += 1

    return (area, points)
