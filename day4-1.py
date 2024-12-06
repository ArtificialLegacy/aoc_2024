def solve(input: str):
    content = input.split("\n")
    assert len(content) > 0

    data = [list(x) for x in content if x != ""]

    count = 0

    for row in range(len(data)):
        rowdata = data[row]
        for col in range(len(rowdata)):
            c = rowdata[col]
            if c != "X" and c != "S":
                continue

            if search_horizontal(row, col, data):
                count += 1
            if search_vertical(row, col, data):
                count += 1
            if search_diagonal_right(row, col, data):
                count += 1
            if search_diagonal_left(row, col, data):
                count += 1

    return count


def test_match(a, b, c, d):
    s = a + b + c + d
    return s == "XMAS" or s == "SAMX"


def search_horizontal(row, col, data):
    rowdata = data[row]
    if col > len(rowdata) - 4:
        return False

    return test_match(
        rowdata[col], rowdata[col + 1], rowdata[col + 2], rowdata[col + 3]
    )


def search_vertical(row, col, data):
    if row > len(data) - 4:
        return False

    return test_match(
        data[row][col], data[row + 1][col], data[row + 2][col], data[row + 3][col]
    )


def search_diagonal_right(row, col, data):
    if row > len(data) - 4:
        return False
    if col > len(data[row]) - 4:
        return False

    return test_match(
        data[row][col],
        data[row + 1][col + 1],
        data[row + 2][col + 2],
        data[row + 3][col + 3],
    )


def search_diagonal_left(row, col, data):
    if row > len(data) - 4:
        return False
    if col < 3:
        return False

    return test_match(
        data[row][col],
        data[row + 1][col - 1],
        data[row + 2][col - 2],
        data[row + 3][col - 3],
    )
