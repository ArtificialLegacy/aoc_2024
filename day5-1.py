import math


def solve(input: str):
    content = input.split("\n")

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

    sum = 0

    for u in updates:
        printed = {}
        correct = True

        for page in u:
            printed[page] = True

            if page in rules:
                for r in rules[page]:
                    if r in printed:
                        correct = False
                        break

        if correct:
            sum += int(u[math.floor(len(u) / 2)])

    return sum
