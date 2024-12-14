import re
import math


def solve(input: str):
    content = input.split("\n")[:-1]
    assert len(content) > 0

    width = 101
    height = 103

    if len(content) == 12:
        width = 11
        height = 7

    halfwidth = math.floor(width / 2)
    halfheight = math.floor(height / 2)

    q1 = 0
    q2 = 0
    q3 = 0
    q4 = 0

    for r in content:
        v = re.findall(r"-?\d+", r)
        assert len(v) == 4

        posx = int(v[0])
        posy = int(v[1])
        velx = int(v[2])
        vely = int(v[3])

        fx = (posx + (velx * 100)) % width
        fy = (posy + (vely * 100)) % height

        if fx < halfwidth and fy < halfheight:
            q1 += 1
        if fx > halfwidth and fy < halfheight:
            q2 += 1
        if fx < halfwidth and fy > halfheight:
            q3 += 1
        if fx > halfwidth and fy > halfheight:
            q4 += 1

    safety = q1 * q2 * q3 * q4
    return safety
