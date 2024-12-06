def solve(input: str):
    content = input.split("\n")
    assert len(content) > 0

    data = [list(x) for x in content if x != ""]

    count = 0

    for rowi in range(len(data) - 2):
        row = rowi + 1
        rowdata = data[row]
        for coli in range(len(rowdata) - 2):
            col = coli + 1
            c = rowdata[col]
            if c != "A":
                continue

            diag1 = check(data[row - 1][col - 1], data[row + 1][col + 1])
            diag2 = check(data[row - 1][col + 1], data[row + 1][col - 1])

            if diag1 and diag2:
                count += 1

    return count


def check(a, b):
    return (a == "M" and b == "S") or (a == "S" and b == "M")
