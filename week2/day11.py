

testfile = 'day11_test_input.txt'


def test_load_input_file():
    assert len(load_input_file(testfile)) == 10

def load_input_file(target):
    with open(target) as f:
        rawlist = [line.strip() for line in f]
    return rawlist

testdata = load_input_file(testfile)

def test_get_slices():
    #test that we can bring back 8 slices from position x, y in 8 radial directions
    assert get_slices(10,12,5,5) == {'left': [(5, 4), (5, 3), (5, 2), (5, 1), (5, 0)], 
                                     'right': [(5, 6), (5, 7), (5, 8), (5, 9), (5, 10), (5, 11)], 
                                     'up': [(4, 5), (3, 5), (2, 5), (1, 5), (0, 5)], 
                                     'down': [(6, 5), (7, 5), (8, 5), (9, 5)],
                                     'downright': [(6, 6), (7, 7), (8, 8), (9, 9)], 
                                     'downleft': [(6, 4), (7, 3), (8, 2), (9, 1)], 
                                     'upright': [(4, 6), (3, 7), (2, 8), (1, 9), (0, 10)], 
                                     'upleft': [(4, 4), (3, 3), (2, 2), (1, 1), (0, 0)]}
    assert get_slices(4,4,0,0) ==  {'left': [], 
                                    'right': [(0, 1), (0, 2), (0, 3)], 
                                    'up': [], 
                                    'down': [(1, 0), (2, 0), (3, 0)], 
                                    'downright': [(1, 1), (2, 2), (3, 3)], 
                                    'downleft': [], 
                                    'upright': [], 
                                    'upleft': []}
    assert get_slices(4,4,3,3) ==  {'left': [(3, 2), (3, 1), (3, 0)], 
                                    'right': [], 
                                    'up': [(2, 3), (1, 3), (0, 3)], 
                                    'down': [], 
                                    'downright': [], 
                                    'downleft': [], 
                                    'upright': [], 
                                    'upleft': [(2, 2), (1, 1), (0, 0)]}   
    assert get_slices(4,4,3,0) ==  {'left': [], 
                                    'right': [(3, 1), (3, 2), (3, 3)], 
                                    'up': [(2, 0), (1, 0), (0, 0)], 
                                    'down': [], 
                                    'downright': [], 
                                    'downleft': [], 
                                    'upright': [(2, 1), (1, 2), (0, 3)], 
                                    'upleft': []}   
    assert get_slices(4,4,0,3) ==  {'left': [(0, 2), (0, 1), (0, 0)], 
                                    'right': [], 
                                    'up': [], 
                                    'down': [(1, 3), (2, 3), (3, 3)], 
                                    'downright': [], 
                                    'downleft': [(1, 2), (2, 1), (3, 0)], 
                                    'upright': [], 
                                    'upleft': []}


def get_slices(sizer, sizec, r, c):
    #get size of array, and position, return slice coordinates
    slices = {}

    #get left slice
    i = r
    if c > 0:
        jrange = list(range(c-1,-1,-1))
    else:
        jrange = []
    irange = [r] * len(jrange)
    slices['left'] = list(zip(irange, jrange))

    #get right slice
    i = r
    if c < sizec -1:
        jrange = list(range(c+1,sizec,1))
    else:
        jrange = []
    irange = [r] * len(jrange)
    slices['right'] = list(zip(irange, jrange))

    #get up slices
    j = c
    if r > 0:
        irange = list(range(r-1,-1,-1))
    else:
        irange = []
    jrange = [c] * len(irange)
    slices['up'] = list(zip(irange, jrange))

    #get down slices
    j = c
    if r < sizer -1:
        irange = list(range(r+1,sizer,1))
    else:
        irange = []
    jrange = [c] * len(irange)
    slices['down'] = list(zip(irange, jrange))

    #downright
    if r < sizer -1:
        irange = list(range(r+1,sizer,1))
    else:
        irange = []
    if c < sizec -1:
        jrange = list(range(c+1,sizec,1))
    else:
        jrange = []
    slices['downright'] = list(zip(irange, jrange))

    #down left
    if r < sizer -1:
        irange = list(range(r+1,sizer,1))
    else:
        irange = []
    if c > 0:
        jrange = list(range(c-1,-1,-1))
    else:
        jrange = []
    slices['downleft'] = list(zip(irange, jrange))

    #upright
    if r > 0:
        irange = list(range(r-1,-1,-1))
    else:
        irange = []
    if c < sizec -1:
        jrange = list(range(c+1,sizec,1))
    else:
        jrange = []
    slices['upright'] = list(zip(irange, jrange))
    
    #upleft
    if r > 0:
        irange = list(range(r-1,-1,-1))
    else:
        irange = []
    if c > 0:
        jrange = list(range(c-1,-1,-1))
    else:
        jrange = []
    slices['upleft'] = list(zip(irange, jrange))
    
    return slices


def test_find_adjacents():
    assert find_adjacents(testdata,0,0) == ['.', 'L', 'L']
    assert find_adjacents(testdata,0,1) == ['L', 'L', 'L', 'L', 'L']
    assert find_adjacents(testdata,0,9) == ['L', 'L', 'L']
    assert find_adjacents(testdata,9,0) == ['.', 'L','.']
    assert find_adjacents(testdata,9,9) == ['L', 'L', '.']
    assert find_adjacents(testdata,2,2) == [ '.', '.','L', 'L', 'L', 'L', 'L', 'L']

def find_adjacents(seatmap, row, col):
    slices = get_slices(len(seatmap), len(seatmap[0]), row, col)
    adjacents = []
    for name, slice in slices.items():
        if len(slice) > 0:
            x = slice[0][0]
            y = slice[0][1]
            adjacents.append(seatmap[x][y])
    
    return adjacents

def test_transform_seatmap():
    round1 = transform_seatmap(testdata)
    assert round1 ==   ['#.##.##.##',
                        '#######.##',
                        '#.#.#..#..',
                        '####.##.##',
                        '#.##.##.##',
                        '#.#####.##',
                        '..#.#.....',
                        '##########',
                        '#.######.#',
                        '#.#####.##']
    round2 = transform_seatmap(round1)
    assert round2 ==   ['#.LL.L#.##', 
                        '#LLLLLL.L#', 
                        'L.L.L..L..', 
                        '#LLL.LL.L#', 
                        '#.LL.LL.LL', 
                        '#.LLLL#.##', 
                        '..L.L.....', 
                        '#LLLLLLLL#', 
                        '#.LLLLLL.L', 
                        '#.#LLLL.##']

def transform_seatmap(seatmap):

    newmap = []
    for rowindex, rowdata in enumerate(seatmap):
        newrow = []
        for colindex, seat in enumerate(rowdata):
            newseat = ''
            adjacents = find_adjacents(seatmap, rowindex, colindex)
            if seat == '.':
                newseat = '.'
            elif seat == 'L':
                if '#' not in adjacents:
                    newseat = '#'
                else:
                    newseat = 'L'
            elif seat == '#':
                if adjacents.count("#") >= 4:
                    newseat = 'L'
                else:
                    newseat = '#'
            newrow.append(newseat)
        newmap.append(''.join(newrow))
    return newmap

test2 = transform_seatmap(testdata)
test3 = transform_seatmap(test2)

def transform_seatmap2(seatmap):

    newmap = []
    for rowindex, rowdata in enumerate(seatmap):
        newrow = []
        for colindex, seat in enumerate(rowdata):
            newseat = ''
            adjacents = find_nearest_seats(seatmap, rowindex, colindex)
            if seat == '.':
                newseat = '.'
            elif seat == 'L':
                if '#' not in adjacents:
                    newseat = '#'
                else:
                    newseat = 'L'
            elif seat == '#':
                if adjacents.count("#") >= 5:
                    newseat = 'L'
                else:
                    newseat = '#'
            newrow.append(newseat)
        newmap.append(''.join(newrow))
    return newmap


def test_repeat_transform():
    assert repeat_transform(testdata) == 37

def repeat_transform(myseats):
    staticseats = False
    oldmap = myseats
    while not staticseats:
        newmap = transform_seatmap(oldmap)
        if oldmap == newmap:
            staticseats = True
        oldmap = newmap
    seatcount = 0
    for line in newmap:
        seatcount += line.count('#')
    return seatcount

def repeat_transform2(myseats):
    staticseats = False
    oldmap = myseats
    while not staticseats:
        newmap = transform_seatmap2(oldmap)
        if oldmap == newmap:
            staticseats = True
        oldmap = newmap
    seatcount = 0
    for line in newmap:
        seatcount += line.count('#')
    return seatcount

def test_find_nearest_seats():
    pass
    assert find_nearest_seats(testdata,0,0) == ['L', 'L', 'L']
    assert find_nearest_seats(testdata,0,1) == ['L', 'L', 'L', 'L', 'L']
    assert find_nearest_seats(testdata,0,9) == ['L', 'L', 'L']
    assert find_nearest_seats(testdata,9,0) == ['L', 'L', 'L']
    assert find_nearest_seats(testdata,9,9) == ['L', 'L', 'L']
    assert find_nearest_seats(testdata,2,2) == ['L', 'L', 'L', 'L', 'L', 'L', 'L', 'L']
    assert find_nearest_seats(test2,2,2) == ['#', '#', '#', '#', '#', '#', '#', '#']
    assert find_nearest_seats(test3,0,9) == ['#', '#', 'L']

def find_nearest_seats(seatmap, row, col):
    nearest_seats = []
    slices = get_slices(len(seatmap), len(seatmap[0]), row, col)
    for name, slice in slices.items():
        for coord in slice:
            x = coord[0]
            y = coord[1] 
            seat = seatmap[x][y]
            if seat != '.':
                nearest_seats.append(seat)
                break
    return nearest_seats


todaylist = load_input_file('day11input.txt')
part1 = repeat_transform(todaylist)
print('part1:', part1)

part2 = repeat_transform2(todaylist)
print('part2:', part2)