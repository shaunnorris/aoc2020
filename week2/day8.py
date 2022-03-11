
import copy
testfile = 'day8_test_input.txt'



def test_load_input_file():
    assert len(load_input_file(testfile)) == 9

def load_input_file(target):
    outputlist = []
    with open(target) as f:
        raw_list = [line.strip() for line in f]
    for line in raw_list:
        outputlist.append(line.split(' '))
    return outputlist

testdata = load_input_file(testfile)


def test_run_commands():
    assert run_commands(testdata) == (5, False)

def run_commands(cmdlist):
    offset = 0
    accumulator = 0
    already_run = []
    noloop = True
    success = False
    while noloop:
        if offset not in already_run:
            if offset < len(cmdlist):
                command = cmdlist[offset][0]
                qty = int(cmdlist[offset][1])
                if command == 'nop':
                    already_run.append(offset)
                    offset += 1
                elif command == 'acc':
                    already_run.append(offset)
                    offset += 1
                    accumulator += qty
                elif command == 'jmp':
                    already_run.append(offset)
                    offset = offset + qty
            elif offset == len(cmdlist):
                return accumulator, True 
        else:
            noloop = False
    return accumulator, success


def test_alter_commands():
    assert alter_commands(testdata) == 8

def alter_commands(cmdlist):
    jmpindices = [i for i, s in enumerate(cmdlist) if 'jmp' in s]
    nopindices = [i for i, s in enumerate(cmdlist) if 'nop' in s]
    indices =  nopindices + jmpindices
    for index in indices:
        thisrun = copy.deepcopy(cmdlist)
        if cmdlist[index][0] == 'jmp':
            thisrun[index][0] = 'nop'
        elif cmdlist[index][0] == 'nop':
            thisrun[index][0] = 'jmp'
        testrun = run_commands(thisrun)
        if testrun[1] == True:
            print('successful run found by changing instruction at', index)
            return testrun[0]

todaylist = load_input_file('day8input.txt')
part1 = run_commands(todaylist)[0]
print('part1:',part1)
part2 = alter_commands(todaylist)
print('part2:',part2)