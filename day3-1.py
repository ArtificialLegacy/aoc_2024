import re


def solve(input):
    file = open(input)
    content = file.read()
    file.close()

    muls = re.findall(r"mul\(\d{0,3},\d{0,3}\)", content, re.MULTILINE)

    total = 0

    for m in muls:
        m = str(m)
        m = m.removeprefix("mul(")
        m = m.removesuffix(")")

        nums = m.split(",")
        assert len(nums) == 2

        total += int(nums[0]) * int(nums[1])

    return total
