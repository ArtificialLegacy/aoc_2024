import re
import sympy as sp


def solve(input: str):
    content = input.split("\n")
    assert len(content) > 0 and len(content) % 4 == 0

    total = 0

    for i in range(0, len(content), 4):
        a = find_numbers(content[i])
        b = find_numbers(content[i + 1])
        p = find_numbers(content[i + 2])
        # ignore errors, lsp is dumb
        p[0] += sp.Rational("10000000000000", "1")
        p[1] += sp.Rational("10000000000000", "1")

        x = (p[1] * b[0] - p[0] * b[1]) / (a[1] * b[0] - a[0] * b[1])
        y = (a[0] * x - p[0]) / b[0]

        # must be done in this order, or will hit edge case where sympy drops the rational
        if x.denominator == 1 and y.denominator == 1:
            total += int(x) * 3 - int(y)

    return total


def find_numbers(s: str):
    nums = re.findall(r"\d+", s)

    v: list[sp.Rational] = [sp.Rational(nums[0], "1"), sp.Rational(nums[1], "1")]
    return v
