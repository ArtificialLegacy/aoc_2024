def solve(input):
    file = open(input)
    content = file.readlines()
    assert len(content) > 0
    file.close()

    data = []

    for line in content:
        nums = line.split()
        assert len(nums) == 2
        data.append([int(nums[0]), int(nums[1])])

    sum = 0

    for n in range(len(data) - 1, 0, -1):
        for i in range(n):
            a = data[i]
            b = data[i + 1]

            if a[0] > b[0]:
                a[0], b[0] = b[0], a[0]
            if a[1] > b[1]:
                a[1], b[1] = b[1], a[1]

        final = data[n]
        dist = abs(final[0] - final[1])
        sum += dist

    final = data[0]
    dist = abs(final[0] - final[1])
    sum += dist

    assert is_sorted(data)
    return sum


def is_sorted(arr):
    for n in range(len(arr) - 1):
        if arr[n][0] > arr[n + 1][0]:
            return False
        if arr[n][1] > arr[n + 1][1]:
            return False

    return True
