testfile = "day13_test_input.txt"


def test_load_input_file():
    assert load_input_file(testfile) == {"buslist": [7, 13, 19, 31, 59], "start": 939}


def load_input_file(target):
    with open(target) as f:
        rawlist = [line.strip() for line in f]
    timetable = {}
    timetable["start"] = int(rawlist[0])
    buslist = rawlist[1].split(",")
    buslist = list(filter(lambda a: a != "x", buslist))
    timetable["buslist"] = sorted(list(map(int, buslist)))
    return timetable


def test_check_timetable():
    assert check_timetable(load_input_file(testfile)) == 295


def check_timetable(timetable):
    waiting = {}
    start_time = timetable["start"]
    for bus in timetable["buslist"]:
        waiting[bus] = bus - start_time % bus
    bestbus = min(waiting, key=waiting.get)
    shortestwait = min(waiting.values())
    return bestbus * shortestwait


todaylist = load_input_file("day13input.txt")
part1 = check_timetable(todaylist)
print("part1:", part1)
