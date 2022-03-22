testfile = "day12_test_input.txt"


def test_load_input_file():
    assert len(load_input_file(testfile)) == 5
    assert load_input_file(testfile) == [
        ("F", 10),
        ("N", 3),
        ("F", 7),
        ("R", 90),
        ("F", 11),
    ]


def load_input_file(target):
    with open(target) as f:
        rawlist = [line.strip() for line in f]
    instructions = []
    for line in rawlist:
        qty = int(line[1:])
        command = line[0]
        instructions.append((command, qty))
    return instructions


leftturns = {}
leftturns["E"] = {}
leftturns["E"][90] = "N"
leftturns["E"][180] = "W"
leftturns["E"][270] = "S"
leftturns["N"] = {}
leftturns["N"][90] = "W"
leftturns["N"][180] = "S"
leftturns["N"][270] = "E"
leftturns["W"] = {}
leftturns["W"][90] = "S"
leftturns["W"][180] = "E"
leftturns["W"][270] = "N"
leftturns["S"] = {}
leftturns["S"][90] = "E"
leftturns["S"][180] = "N"
leftturns["S"][270] = "W"


def test_translate_to_absolute():
    assert translate_to_absolute(load_input_file(testfile)) == [
        ("E", 10),
        ("N", 3),
        ("E", 7),
        ("S", 11),
    ]


def translate_to_absolute(instructions):
    new_instructions = []
    current_heading = "E"
    for instruction in instructions:
        command = instruction[0]
        qty = instruction[1]
        if command in ["N", "S", "E", "W"]:
            new_instructions.append((command, qty))
        elif command == "F":
            new_instructions.append((current_heading, qty))
        elif command == "L":
            current_heading = leftturns[current_heading][qty]
        elif command == "R":
            current_heading = leftturns[current_heading][360 - qty]
    return new_instructions


def test_navigate():
    assert navigate(translate_to_absolute(load_input_file(testfile))) == 25


def navigate(abs_ins):
    position = {}
    position["N"] = 0
    position["E"] = 0
    for instruction in abs_ins:
        command = instruction[0]
        qty = instruction[1]
        if command == "N":
            position["N"] += qty
        elif command == "S":
            position["N"] -= qty
        elif command == "E":
            position["E"] += qty
        elif command == "W":
            position["E"] -= qty

    return abs(position["N"]) + abs(position["E"])


def test_follow_waypoint():
    assert follow_waypoint(load_input_file(testfile)) == 286


def follow_waypoint(instructions):
    ship = {}
    ship["N"] = 0
    ship["E"] = 0
    wayp = {}
    wayp["N"] = 1
    wayp["E"] = 10
    for instruction in instructions:
        command = instruction[0]
        qty = instruction[1]
        if command == "N":
            wayp["N"] += qty
        elif command == "S":
            wayp["N"] -= qty
        elif command == "E":
            wayp["E"] += qty
        elif command == "W":
            wayp["E"] -= qty
        elif command in ["L", "R"]:
            wayp = rotate_wayp(wayp, command, qty)
        elif command == "F":
            ship["E"] = ship["E"] + wayp["E"] * qty
            ship["N"] = ship["N"] + wayp["N"] * qty
    # print('wp',wayp)
    # print('ship',ship)
    return abs(ship["N"]) + abs(ship["E"])


def test_rotate_wayp():
    test_wp = {"N": 7, "E": 13}
    assert rotate_wayp(test_wp, "L", 90) == {"N": 13, "E": -7}
    assert rotate_wayp(test_wp, "L", 180) == {"N": -7, "E": -13}
    assert rotate_wayp(test_wp, "L", 270) == {"E": 7, "N": -13}
    assert rotate_wayp(test_wp, "R", 90) == {"E": 7, "N": -13}
    assert rotate_wayp(test_wp, "R", 180) == {"N": -7, "E": -13}
    assert rotate_wayp(test_wp, "R", 270) == {"N": 13, "E": -7}


def rotate_wayp(wp, cmd, qty):
    if cmd == "R":
        cmd = "L"
        qty = 360 - qty
    if qty == 90:
        newnorth = wp["E"]
        neweast = -wp["N"]
    elif qty == 180:
        newnorth = -wp["N"]
        neweast = -wp["E"]
    elif qty == 270:
        newnorth = -wp["E"]
        neweast = wp["N"]
    return {"N": newnorth, "E": neweast}


todaylist = load_input_file("day12input.txt")
part1 = navigate(translate_to_absolute(todaylist))
print("part1:", part1)
part2 = follow_waypoint(todaylist)
print("part2:", part2)
