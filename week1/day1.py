small_test_data = [
    1721,
    979,
    366,
    299,
    675,
    1456,
]


def test_find_add_pair_product():
    assert find_add_pair_product(small_test_data, 2020) == 514579
    assert find_add_pair_product(small_test_data, 2021) == False


def find_add_pair_product(list, target):
    checked = {}
    for element in list:
        if (target - element) in checked.keys():
            return element * (target - element)
        else:
            checked[element] = True
    return False


def test_find_add_triple_product():
    assert find_add_triple_product(small_test_data, 2020) == 241861950


def find_add_triple_product(list, target):
    checked = {}
    for element in list:
        check_pair = find_add_pair_product(list, (target - element))
        if check_pair != False:
            return element * check_pair


def test_load_input_file():
    assert len(load_input_file_to_list("day1_test_input.txt")) == 6
    assert load_input_file_to_list("day1_test_input.txt") == small_test_data


def load_input_file_to_list(target):
    with open(target) as f:
        raw_list = [line.strip() for line in f]
        integer_map = map(int, raw_list)
        integer_list = list(integer_map)
    return integer_list


part1_list = load_input_file_to_list("day1input.txt")
part1_solution = find_add_pair_product(part1_list, 2020)
print("part1:", part1_solution)

part2_list = part1_list
part2_solution = find_add_triple_product(part2_list, 2020)
print("part2:", part2_solution)
