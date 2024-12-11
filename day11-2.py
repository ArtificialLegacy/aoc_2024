def solve(input: str):
    content = input.split()
    assert len(content) > 0

    count = len(content)

    for s in content:
        count += step((int(s), 0))

    return count


cache: dict[tuple[int, int], int] = {}


def step(stone: tuple[int, int]):
    count = 0

    if stone[1] >= 75:
        return 0

    if stone in cache:
        return cache[stone]

    value = stone[0]
    age = stone[1]

    if value == 0:
        count += step((1, age + 1))
    elif len(str(value)) % 2 == 0:
        sv = str(value)
        svl = int(len(sv) / 2)

        count += step((int(sv[svl:]), age + 1)) + 1
        count += step((int(sv[:svl]), age + 1))
    else:
        count += step((value * 2024, age + 1))

    cache[stone] = count
    return count
