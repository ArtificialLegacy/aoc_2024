def solve(input: str):
    content = input.split("\n")
    assert len(content) > 0

    count = 0

    for report in content:
        if report == "":
            break

        safe = True
        s = 0

        levels = report.split()
        for n in range(len(levels) - 1):
            a = int(levels[n])
            b = int(levels[n + 1])

            if a == b:
                safe = False
                break

            change = a - b

            if s == 0:
                s = sign(change)
            elif s != sign(change):
                safe = False
                break

            if abs(change) > 3:
                safe = False
                break

        if safe:
            count += 1

    return count


def sign(x):
    return (x > 0) - (x < 0)
