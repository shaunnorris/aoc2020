import collections

testfile = "day9_test_input.txt"


def test_load_input_file():
    assert len(load_input_file(testfile)) == 20


def load_input_file(target):
    with open(target) as f:
        return [int(line.strip()) for line in f]


test_data = load_input_file(testfile)


def test_find_add_pair_product():
    assert find_add_pair_product(test_data[0:4], test_data[5]) == (True, 25, 15)
    assert find_add_pair_product(test_data[0:4], 999) == (False, 0, 0)


def find_add_pair_product(list, target):
    checked = {}
    for element in list:
        if (target - element) in checked.keys() and target - element != element:
            return (True, element, (target - element))
        else:
            checked[element] = True
    return (False, 0, 0)


def test_walk_list():
    assert walk_list(test_data, 5) == 127


def walk_list(mylist, preamble):
    offset = preamble
    while offset < len(mylist):
        check_valid = find_add_pair_product(
            mylist[offset - preamble : offset], mylist[offset]
        )
        if not check_valid[0]:
            return mylist[offset]
        else:
            offset += 1


def test_find_sublist():
    assert find_sublist(test_data, 127) == 62


def find_sublist(mylist, target):
    dq = collections.deque()
    offset = 0

    while sum(dq) != target:

        if sum(dq) < target:
            dq.append(mylist[offset])
            offset += 1
        elif sum(dq) > target:
            dq.popleft()

    if sum(dq) == target:
        return min(dq) + max(dq)
    else:
        return False


todaylist = load_input_file("day9input.txt")
part1 = walk_list(todaylist, 25)
print("part1:", part1)
part2 = find_sublist(todaylist, part1)
print("part2:", part2)
