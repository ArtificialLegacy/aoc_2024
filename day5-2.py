import math


def solve(input: str):
    content = input.split("\n")[:-1]
    assert len(content) > 0

    rules = {}
    updates = []

    chunk = 0
    for line in content:
        if line == "":
            chunk += 1
        elif chunk == 0:
            nums = line.split("|")
            assert len(nums) == 2

            if nums[0] not in rules:
                rules[nums[0]] = [nums[1]]
            else:
                rules[nums[0]].append(nums[1])
        elif chunk == 1:
            updates.append(line.split(","))

    assert len(updates) > 0
    sum = 0

    for u in updates:
        correct = True
        sorted = False

        while not sorted:
            printed = {}
            sorted = True

            for i in range(len(u)):
                page = u[i]
                printed[page] = True

                if not check(page, rules, printed):
                    correct, sorted = False, False
                    u[i], u[i - 1] = u[i - 1], u[i]

        if correct:
            continue

        sum += int(u[math.floor(len(u) / 2)])

    return sum


def check(page, rules, printed):
    if page in rules:
        for r in rules[page]:
            if r in printed:
                return False

    return True
