def solve(input: str):
    input = input[:-1]

    map: list[tuple[int, int, bool]] = []

    empty = False
    idx = 0
    for i in range(len(input)):
        val = int(input[i])
        if empty:
            map.append((-1, val, True))
        else:
            map.append((idx, val, False))
            idx += 1

        empty = not empty

    for i in range(len(map) - 1, 1, -1):
        file = map[i]
        if file[2]:
            continue

        for x in range(1, i, 1):
            if map[x][0] != -1:
                continue

            empty = map[x]
            el = empty[1]
            fl = file[1]

            if el > fl:
                map[x + 1 : x + 1] = [(-1, el - fl, True)]
                map[i + 1] = (-1, fl, True)
            elif el == fl:
                map[i] = (-1, fl, True)
            else:
                continue

            map[x] = (file[0], fl, True)
            break

    checksum = 0

    ps = map[0][1]
    for v in map[1:]:
        if v[0] == -1:
            ps += v[1]
            continue

        fs = v[0]
        ln = v[1]
        checksum += ln * fs * ps + (fs * (ln**2 - ln)) / 2
        ps += ln

    return int(checksum)
