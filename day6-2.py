import copy


def solve(input: str):
    content = input.split("\n")
    assert len(content) > 0

    values = {"#": 0, ".": 1, "^": 2, ">": 3, "V": 5, "<": 7}

    grid = [[values[c] for c in list(x)] for x in content if x != ""]

    guard = guard_find(grid)
    assert guard is not None

    count = 0

    while guard.active:
        grid[guard.row][guard.col] *= guard.c

        pos = guard.next()

        if not in_bounds(grid, pos):
            guard.active = False
            break

        gdata = grid[pos[0]][pos[1]]

        if gdata == 1:
            checkGrid = copy.deepcopy(grid)
            checkGrid[pos[0]][pos[1]] = 0
            loop = trace(checkGrid, guard.clone())
            if loop:
                count += 1

        if gdata == 0:
            guard.rotate()
        else:
            guard.row = pos[0]
            guard.col = pos[1]

    return count


def guard_find(grid: list[list[int]]):
    for row in range(len(grid)):
        rowdata = grid[row]
        for col in range(len(rowdata)):
            coldata = rowdata[col]
            if coldata in (2, 3, 5, 7):
                grid[row][col] = 1
                return Guard(coldata, row, col)

    return None


def trace(grid: list[list[int]], guard):
    while guard.active:
        pos = guard.next()

        if not in_bounds(grid, pos):
            guard.active = False
            return False

        gdata = grid[pos[0]][pos[1]]

        if gdata > 1 and gdata % guard.c == 0:
            return True
        elif gdata == 0:
            guard.rotate()
        else:
            guard.row = pos[0]
            guard.col = pos[1]
            grid[guard.row][guard.col] *= guard.c

    return False


def in_bounds(grid, pos):
    return 0 <= pos[0] < len(grid) and 0 <= pos[1] < len(grid[pos[0]])


class Guard:
    def __init__(self, c, row, col):
        assert c in (2, 3, 5, 7)

        self.c = c
        self.row = row
        self.col = col
        self.active = True

    def clone(self):
        return Guard(self.c, self.row, self.col)

    def next(self):
        pos = [self.row, self.col]

        if self.c == 2:
            pos[0] -= 1
        elif self.c == 5:
            pos[0] += 1
        elif self.c == 7:
            pos[1] -= 1
        elif self.c == 3:
            pos[1] += 1

        return pos

    def rotate(self):
        next = {2: 3, 3: 5, 5: 7, 7: 2}
        self.c = next[self.c]
