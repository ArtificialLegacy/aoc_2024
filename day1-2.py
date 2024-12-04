def solve(input):
    file = open(input)
    content = file.readlines()
    assert len(content) > 0
    file.close()

    list1 = []
    list2 = []

    for line in content:
        nums = line.split()
        assert len(nums) == 2
        list1.append(int(nums[0]))
        list2.append(int(nums[1]))

    sum = 0
    found = {}

    for num in list1:
        if num in found:
            sum += num * found[num]
        else:
            count = count_val(list2, num)
            sum += num * count
            found[num] = count

    return sum


def count_val(arr, val):
    count = 0
    for num in arr:
        if num == val:
            count += 1

    return count
