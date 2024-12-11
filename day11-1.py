def solve(input: str):
    content = input.split()
    assert len(content) > 0

    count = 0

    for s in content:
        count += step((int(s), 0))

    return count


def step(stone: tuple[int, int]):
    count = 1

    while stone[1] < 25:
        value = stone[0]

        if value == 0:
            stone = (1, stone[1] + 1)
        elif len(str(value)) % 2 == 0:
            sv = str(value)
            svl = int(len(sv) / 2)

            count += step((int(sv[:svl]), stone[1] + 1)) - 1
            count += step((int(sv[svl:]), stone[1] + 1)) - 1
            count += 1
            break
        else:
            stone = (value * 2024, stone[1] + 1)

    return count
