import re


def solve(input: str):
    content = input.split("\n")
    assert len(content) > 0 and len(content) % 4 == 0

    total = 0

    for i in range(0, len(content), 4):
        a = find_numbers(content[i])
        b = find_numbers(content[i + 1])
        p = find_numbers(content[i + 2])

        x = (p[1] * b[0] - p[0] * b[1]) / (a[1] * b[0] - a[0] * b[1])
        y = (a[0] * x - p[0]) / b[0]

        t = 3 * x - y
        if int(t) == t:
            total += int(t)

    return total


def find_numbers(s: str):
    nums = re.findall(r"\d+", s)
    assert len(nums) == 2

    return [float(nums[0]), float(nums[1])]
