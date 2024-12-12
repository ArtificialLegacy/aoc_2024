def solve(input: str):
    content = input.split("\n")[:-1]
    assert len(content) > 0

    map: list[list[tuple[int, bool]]] = []

    for row in range(len(content)):
        rowdata = content[row]
        map.append([])
        for col in range(len(rowdata)):
            coldata = rowdata[col]
            map[row].append((ord(coldata), False))

    price = 0

    for row in range(len(map)):
        for col in range(len(map[row])):
            if not map[row][col][1]:
                d = count(map, row, col)
                price += d[0] * d[1]

    return price


def count(map: list[list[tuple[int, bool]]], row: int, col: int):
    area = 1
    perimeter = 0

    value = map[row][col]

    map[row][col] = (value[0], True)

    if row > 0:
        if map[row - 1][col][0] != value[0]:
            perimeter += 1
        elif not map[row - 1][col][1]:
            d = count(map, row - 1, col)
            area += d[0]
            perimeter += d[1]
    else:
        perimeter += 1

    if row < len(map) - 1:
        if map[row + 1][col][0] != value[0]:
            perimeter += 1
        elif not map[row + 1][col][1]:
            d = count(map, row + 1, col)
            area += d[0]
            perimeter += d[1]
    else:
        perimeter += 1

    if col > 0:
        if map[row][col - 1][0] != value[0]:
            perimeter += 1
        elif not map[row][col - 1][1]:
            d = count(map, row, col - 1)
            area += d[0]
            perimeter += d[1]
    else:
        perimeter += 1

    if col < len(map[row]) - 1:
        if map[row][col + 1][0] != value[0]:
            perimeter += 1
        elif not map[row][col + 1][1]:
            d = count(map, row, col + 1)
            area += d[0]
            perimeter += d[1]
    else:
        perimeter += 1

    return (area, perimeter)
