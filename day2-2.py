def solve(input: str):
    content = input.split("\n")[:-1]
    assert len(content) > 0

    count = 0

    for report in content:
        levels = report.split()
        if check(levels):
            count += 1
            continue

        for n in range(len(levels)):
            cut = report.split()
            cut.pop(n)
            if check(cut):
                count += 1
                break

    return count


def check(levels):
    safe = True
    s = 0

    for n in range(len(levels) - 1):
        a = int(levels[n])
        b = int(levels[n + 1])

        if is_safe(a, b, s):
            if s == 0:
                s = sign(a - b)
        else:
            safe = False

    return safe


def is_safe(a, b, s):
    change = a - b

    if change == 0:
        return False

    if s != 0 and s != sign(change):
        return False

    if abs(change) > 3:
        return False

    return True


def sign(x):
    return (x > 0) - (x < 0)
