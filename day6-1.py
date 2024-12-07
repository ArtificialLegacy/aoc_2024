def solve(input: str):
    content = input.split("\n")
    assert len(content) > 0

    grid = [list(x) for x in content if x != ""]

    guard = guard_find(grid)
    assert guard is not None

    while guard.active:
        grid[guard.row][guard.col] = "X"

        pos = guard.next()

        if not in_bounds(grid, pos):
            guard.active = False
        elif grid[pos[0]][pos[1]] == "#":
            guard.rotate()
        else:
            guard.row = pos[0]
            guard.col = pos[1]

    positions = [x for y in grid for x in y if x == "X"]
    return len(positions)


def guard_find(grid: list[list[str]]):
    for row in range(len(grid)):
        rowdata = grid[row]
        for col in range(len(rowdata)):
            coldata = rowdata[col]
            if coldata in ("^", ">", "V", "<"):
                return Guard(coldata, row, col)

    return None


def in_bounds(grid, pos):
    return 0 <= pos[0] < len(grid) and 0 <= pos[1] < len(grid[pos[0]])


class Guard:
    def __init__(self, c, row, col):
        assert c in ("^", ">", "V", "<")

        self.c = c
        self.row = row
        self.col = col
        self.active = True

    def next(self):
        pos = [self.row, self.col]

        if self.c == "^":
            pos[0] -= 1
        elif self.c == "V":
            pos[0] += 1
        elif self.c == "<":
            pos[1] -= 1
        elif self.c == ">":
            pos[1] += 1

        return pos

    def rotate(self):
        next = {"^": ">", ">": "V", "V": "<", "<": "^"}
        self.c = next[self.c]
