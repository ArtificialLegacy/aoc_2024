def solve(input: str):
    input = input[:-1]

    map: list[int] = []

    idx = 0
    empty = False
    for f in input:
        if empty:
            map.extend([-1 for _ in range(int(f))])
        else:
            map.extend([idx for _ in range(int(f))])
            idx += 1

        empty = not empty

    cursa = 0
    cursb = len(map) - 1

    while cursa != cursb:
        while map[cursa] != -1 and cursa != cursb:
            cursa += 1

        if cursa == cursb:
            break

        map[cursa] = map[cursb]
        map[cursb] = -1
        cursb -= 1

    checksum = 0

    for i in range(len(map)):
        val = map[i]
        if val == -1:
            break

        checksum += val * i

    return checksum
