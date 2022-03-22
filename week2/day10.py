from collections import Counter

testfile = "day10_test_input.txt"
testfile2 = "day10_test_input2.txt"


def test_load_input_file():
    assert len(load_input_file(testfile)) == 13


def load_input_file(target):
    with open(target) as f:
        rawlist = [int(line.strip()) for line in f]
        rawlist.append(0)
        rawlist.append(max(rawlist) + 3)
        return sorted(rawlist)


testdata = load_input_file(testfile)
testdata2 = load_input_file(testfile2)


def test_analyze_list():
    assert analyze_list(testdata) == 35
    assert analyze_list(testdata2) == 220


def analyze_list(mylist):
    offset = 0
    differences = {}
    differences["1"] = 0
    differences["3"] = 0
    while offset < len(mylist) - 1:
        difference = mylist[offset + 1] - mylist[offset]
        differences[str(difference)] += 1
        offset += 1
    return differences["1"] * differences["3"]


def test_analyze_options():
    assert analyze_options(testdata) == 8
    assert analyze_options(testdata2) == 19208


def analyze_options(mylist):
    # with credit to: https://github.com/elvinyhlee/advent-of-code-2020-python/blob/master/day10.py
    dp = Counter()
    dp[0] = 1

    for element in mylist[1:]:
        dp[element] = dp[element - 1] + dp[element - 2] + dp[element - 3]
    return dp[max(dp)]


todaylist = load_input_file("day10input.txt")
part1 = analyze_list(todaylist)
print("part1:", part1)
part2 = analyze_options(todaylist)
print("part2", int(part2))
