test_file = "day5_test_input.txt"

test_data = [
    "FBFBBFFRLR",
    "BFFFBBFRRR",
    "FFFBBBFRRR",
    "BBFFBBFRLL",
]


def test_load_input_file():
    assert len(load_input_file_to_list(test_file)) == 4
    assert load_input_file_to_list(test_file) == test_data


def load_input_file_to_list(target):
    with open(target) as f:
        raw_list = [line.strip() for line in f]
    return raw_list


def test_decode_id():
    assert decode_id(test_data) == [357, 567, 119, 820]


def decode_id(seatcodes):
    id_list = []
    for seatcode in seatcodes:
        rowcode = seatcode[:7]
        columncode = seatcode[7:]
        rowcode = rowcode.replace("F", "0")
        rowcode = rowcode.replace("B", "1")
        columncode = columncode.replace("L", "0")
        columncode = columncode.replace("R", "1")
        row = int(rowcode, 2)
        column = int(columncode, 2)
        seatid = row * 8 + column
        id_list.append(seatid)
    return id_list


def find_missing(id_list):
    missing_list = []
    for row in range(0, 127):
        for column in range(0, 7):
            check_id = row * 8 + column
            if check_id not in id_list:
                missing_list.append(check_id)
    for missing_seat in missing_list:
        if missing_seat - 1 in id_list and missing_seat + 1 in id_list:
            return missing_seat


today_input = "day5input.txt"
seatpass_list = load_input_file_to_list(today_input)
seat_ids = decode_id(seatpass_list)
part1 = max(seat_ids)
part2 = find_missing(seat_ids)

print("part1:", part1)
print("part2:", part2)
