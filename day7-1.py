def solve(input: str):
    content = input.split("\n")[:-1]
    assert len(content) > 0

    sum = 0

    for test in content:
        d = test.split(":")
        assert len(d) == 2

        value = int(d[0])
        nums = [int(x) for x in d[1].split()]

        if step(value, nums[0], nums[1:], "+"):
            sum += value
        elif step(value, nums[0], nums[1:], "*"):
            sum += value

    return sum


def step(goal: int, current: int, nums: list[int], operator: str):
    if operator == "+":
        current += nums[0]
    elif operator == "*":
        current *= nums[0]

    if len(nums) == 1:
        return current == goal
    if current > goal:
        return False

    return step(goal, current, nums[1:], "+") or step(goal, current, nums[1:], "*")
