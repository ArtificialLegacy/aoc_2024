import re


def solve(pinput: str):
    content = pinput.split("\n")[:-1]
    assert len(content) > 0

    width = 101
    height = 103

    if len(content) == 12:
        width = 11
        height = 7

    robots: list[Robot] = []

    map: list[list[int]] = []

    for _ in range(width):
        map.append([0 for _ in range(height)])

    for r in content:
        rob = Robot(r)
        robots.append(rob)
        map[rob.posx][rob.posy] += 1

    done = False
    count = 0

    while not done:
        count += 1

        for r in robots:
            r.step(map, width, height)

        rvalue = 0

        for row in map:
            rv = 0
            for col in row:
                if col != 0:
                    rv += 1
                else:
                    if rv > rvalue:
                        rvalue = rv
                    rv = 0

        if rvalue > width / 4:
            for row in map:
                for col in row:
                    if col == 0:
                        print(" ", end="")
                    else:
                        print(col, end="")
                print("")

            q = input("step " + str(count) + " (y):")
            if q == "y":
                done = True

    return count


class Robot:
    def __init__(self, s: str):
        v = re.findall(r"-?\d+", s)
        assert len(v) == 4

        self.posx = int(v[0])
        self.posy = int(v[1])
        self.velx = int(v[2])
        self.vely = int(v[3])

    def step(self, map: list[list[int]], width: int, height: int):
        map[self.posx][self.posy] -= 1

        self.posx = (self.posx + self.velx) % width
        self.posy = (self.posy + self.vely) % height

        map[self.posx][self.posy] += 1
