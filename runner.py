import sys
import importlib


def get_example(day, part):
    file = open(f"./examples/day{day}-{part}_output.txt")
    content = file.read()
    file.close()

    assert content != ""
    return int(content)


assert len(sys.argv) == 3
day = int(sys.argv[1])
assert day > 0 and day < 26
part = int(sys.argv[2])
assert part == 1 or part == 2

daymod = importlib.import_module(f"day{day}-{part}")

example = daymod.solve(f"./examples/day{day}_input.txt")
answer = get_example(day, part)
assert example == answer

result = daymod.solve(f"./input/day{day}.txt")
print(f"result: {result}")
