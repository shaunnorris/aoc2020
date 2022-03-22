test_data = [
    "..##.......",
    "#...#...#..",
    ".#....#..#.",
    "..#.#...#.#",
    ".#...##..#.",
    "..#.##.....",
    ".#.#.#....#",
    ".#........#",
    "#.##...#...",
    "#...##....#",
    ".#..#...#.#",
]

test_coords = [
    [0, 2],
    [0, 3],
    [1, 0],
    [1, 4],
    [1, 8],
    [2, 1],
    [2, 6],
    [2, 9],
    [3, 2],
    [3, 4],
    [3, 8],
    [3, 10],
    [4, 1],
    [4, 5],
    [4, 6],
    [4, 9],
    [5, 2],
    [5, 4],
    [5, 5],
    [6, 1],
    [6, 3],
    [6, 5],
    [6, 10],
    [7, 1],
    [7, 10],
    [8, 0],
    [8, 2],
    [8, 3],
    [8, 7],
    [9, 0],
    [9, 4],
    [9, 5],
    [9, 10],
    [10, 1],
    [10, 4],
    [10, 8],
    [10, 10],
]

test_file = "day3_test_input.txt"


def test_load_input_file():
    assert len(load_input_file_to_list(test_file)) == 11
    assert load_input_file_to_list(test_file) == test_data


def load_input_file_to_list(target):
    with open(target) as f:
        raw_list = [line.strip() for line in f]
    return raw_list


def test_raw_to_coords():
    assert raw_to_coords(test_data) == test_coords
    assert len(raw_to_coords(test_data)) == 37


def raw_to_coords(treelist):
    coords = []
    for x, row in enumerate(treelist):
        for y, character in enumerate(row):
            if character == "#":
                coords.append([x, y])
    return coords


def test_find_shape():
    assert find_shape(test_data) == [11, 11]


def find_shape(treemap):
    return [len(treemap), len(treemap[0])]


def test_find_trees():
    assert find_trees(test_coords, 3, 1, [11, 11]) == 7


def find_trees(coords, across, down, shape):
    x_pos = 0
    y_pos = 0
    trees = 0
    while x_pos < shape[0]:
        if y_pos >= shape[1]:
            y_pos = y_pos - shape[1]
        if [x_pos, y_pos] in coords:
            trees += 1
        x_pos = x_pos + down
        y_pos = y_pos + across
    return trees


def test_part2():
    assert find_all_paths(test_coords, [11, 11]) == 336


def find_all_paths(coords, shape):
    part2_offsets = [
        [1, 1],
        [3, 1],
        [5, 1],
        [7, 1],
        [1, 2],
    ]
    product = 1
    for offset in part2_offsets:
        treecount = find_trees(coords, offset[0], offset[1], shape)
        product = product * treecount
    return product


treemap = load_input_file_to_list("day3input.txt")
shape = find_shape(treemap)
coords = raw_to_coords(treemap)
part1 = find_trees(coords, 3, 1, shape)
print("part1:", part1)
part2 = find_all_paths(coords, shape)
print("part2:", part2)
