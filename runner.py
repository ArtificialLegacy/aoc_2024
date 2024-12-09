import sys
import importlib
import time


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

examplefile = open(f"./examples/day{day}-{part}_input.txt")
example_input = examplefile.read()
examplefile.close()

example = daymod.solve(example_input)
answer = get_example(day, part)
assert example == answer

puzzlefile = open(f"./input/day{day}.txt")
puzzle_input = puzzlefile.read()
puzzlefile.close()

start = time.time()
result = daymod.solve(puzzle_input)
end = time.time()
print(f"\nresult: {result}")
print("in: %s" % (end - start))
