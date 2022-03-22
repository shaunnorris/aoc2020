test_data = [
    "1-3 a: abcde",
    "1-3 b: cdefg",
    "2-9 c: ccccccccc",
]

test_file = "day2_test_input.txt"


def test_load_input_file():
    assert len(load_input_file_to_list(test_file)) == 3
    assert load_input_file_to_list(test_file) == test_data


def load_input_file_to_list(target):
    with open(target) as f:
        raw_list = [line.strip() for line in f]
    return raw_list


def test_check_policy():
    assert check_policy(test_data) == 2


def check_policy(pwlist):
    valid = 0
    for element in pwlist:
        element_list = element.split(" ")
        range = element_list[0].split("-")
        low = int(range[0])
        high = int(range[1])
        character = element_list[1][0]
        password = element_list[2]
        if low <= password.count(character) <= high:
            valid += 1
    return valid


def test_part2_policy():
    assert check_part2_policy(test_data) == 1


def check_part2_policy(pwlist):
    valid = 0
    for element in pwlist:
        element_list = element.split(" ")
        range = element_list[0].split("-")
        first = int(range[0]) - 1
        second = int(range[1]) - 1
        character = element_list[1][0]
        password = element_list[2]
        subpass = password[first] + password[second]
        if subpass.count(character) == 1:
            valid += 1
    return valid


day_list = load_input_file_to_list("day2input.txt")
part1 = check_policy(day_list)
print("part1:", part1)
part2 = check_part2_policy(day_list)
print("part2", part2)
