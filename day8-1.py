def solve(input: str):
    content = input.split("\n")[:-1]
    assert len(content) > 0

    nodes: dict[str, list[Node]] = {}

    width = len(content)
    height = len(content[0])

    for row in range(width):
        rowdata = content[row]
        for col in range(height):
            cell = rowdata[col]
            if cell != ".":
                if cell in nodes:
                    nodes[cell].append(Node(cell, row, col))
                else:
                    nodes[cell] = [Node(cell, row, col)]

    assert len(nodes) > 0

    antinodes: dict[tuple[int, int], bool] = {}

    for t in nodes:
        for node in nodes[t]:
            for other in nodes[t]:
                if node is other:
                    continue

                slope = node.slope(other)
                if in_bounds(slope, width, height):
                    antinodes[slope] = True

    return len(antinodes)


def in_bounds(p: tuple[int, int], width: int, height: int):
    return 0 <= p[0] < width and 0 <= p[1] < height


class Node:
    def __init__(self, signal: str, row: int, col: int):
        self.signal = signal
        self.row = row
        self.col = col

    def slope(self, to):
        return (self.row - (to.row - self.row), self.col - (to.col - self.col))
