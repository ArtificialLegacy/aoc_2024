def solve(input: str):
    input = input[:-1]

    map: list[tuple[int, int, bool, int]] = []

    empty = False
    idx = 0
    ps = 0
    for i in range(len(input)):
        val = int(input[i])
        if empty:
            map.append((-1, val, True, ps))
        else:
            map.append((idx, val, False, ps))
            idx += 1

        ps += val
        empty = not empty

    checksum = 0

    for i in range(len(map) - 1, 1, -1):
        file = map[i]
        if file[2]:
            continue

        fs = file[0]
        fl = file[1]
        fp = file[3]

        for x in range(1, i, 1):
            if map[x][0] != -1:
                continue

            empty = map[x]
            el = empty[1]
            ep = empty[3]

            if el > fl:
                map[x + 1 : x + 1] = [(-1, el - fl, True, ep + fl)]
                map[i + 1] = empty
            elif el == fl:
                map[i] = empty
            else:
                continue

            map[x] = (fs, fl, True, ep)
            fp = ep
            break

        checksum += fl * fs * fp + (fs * (fl**2 - fl)) / 2

    return int(checksum)
