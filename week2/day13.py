testfile = "day13_test_input.txt"


def test_load_input_file():
    assert load_input_file(testfile) == {"buslist": [7, 13, 19, 31, 59], "start": 939}
    assert load_input_file(testfile, 2) == [7, 13, "x", "x", 59, "x", 31, 19]


def load_input_file(target, part=1):
    with open(target) as f:
        rawlist = [line.strip() for line in f]
    if part == 1:
        timetable = {}
        timetable["start"] = int(rawlist[0])
        buslist = rawlist[1].split(",")
        buslist = list(filter(lambda a: a != "x", buslist))
        timetable["buslist"] = sorted(list(map(int, buslist)))
        return timetable
    elif part == 2:
        buslist = ["x" if x == "x" else int(x) for x in rawlist[1].split(",")]
        return buslist


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


def test_check_coincidence():
    assert check_coincidence(load_input_file(testfile, 2)) == 1068781


def check_coincidence(buslist):
    # credit goes to: https://dev.to/qviper/advent-of-code-2020-python-solution-day-13-24k4
    # which makes use of https://en.wikipedia.org/wiki/Chinese_remainder_theorem
    mods = {bus: -i % bus for i, bus in enumerate(buslist) if bus != "x"}
    vals = list(reversed(sorted(mods)))
    val = mods[vals[0]]
    r = vals[0]
    for b in vals[1:]:
        while val % b != mods[b]:
            val += r
        r *= b
    return val


inputfile = "day13input.txt"

todaylist1 = load_input_file(inputfile)
todaylist2 = load_input_file(inputfile, 2)

part1 = check_timetable(todaylist1)
print("part1:", part1)
part2 = check_coincidence(todaylist2)
print("part2:", part2)
