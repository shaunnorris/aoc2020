import pytest


test_data = ['abc', 'abc', 'abac', 'aaaa', 'b']
test_data2 = ['abc', '', 'a', 'a', 'b']

test_file = 'day6_test_input.txt'

def test_load_input_file2():
    test_list = load_input_file2(test_file)
    assert len(test_list) == 5
    assert test_list == test_data2

def load_input_file2(target):

    def add_to_list(group,groupcount):
        answers = ''
        for key,value in group.items():
            if value == groupcount:
                answers = answers + key
        shortlist.append(answers)

    f = open(target, 'r+')
    longline = ''
    shortlist = []
    group = {}
    groupcount = 0
    for line in f.readlines():
        line = line.strip()
        if line != '':
            groupcount += 1
            for character in line:
                if character in group.keys():
                    group[character] += 1
                else:
                    group[character] = 1
        else:
            add_to_list(group, groupcount)
            groupcount = 0
            group = {}
    f.close()
    add_to_list(group, groupcount)
    return shortlist

def test_load_input_file():
    test_list = load_input_file(test_file) 
    assert len(test_list) == 5
    assert test_list == test_data
    
def load_input_file(target):
    f = open(target, 'r+')
    longline = ''
    shortlist = []
    for line in f.readlines():
        line = line.strip()
        if line != '':
            if len(longline) > 0:
                longline = longline + line
            else:
                longline = line
        else:
            
            shortlist.append(longline)
            longline = ''
    f.close()
    shortlist.append(longline)
    return shortlist

def test_remove_duplicates():
    assert remove_duplicates(test_data) == ['abc', 'abc','abc', 'a', 'b']
    
def remove_duplicates(dupelist):
    shortlist = []
    for element in dupelist:     
        dedupe = "".join(dict.fromkeys(element))
        shortlist.append(dedupe)
    return shortlist

def test_count_unique_answers():
    dedupelist = remove_duplicates(test_data)
    assert count_unique_answers(dedupelist) == 11

def count_unique_answers(dedupe_list):
    count = 0
    for element in dedupe_list:
        count += len(element)
    return count#

targetfile = 'day6input.txt'
answerlist = remove_duplicates(load_input_file(targetfile))
part1 = count_unique_answers(answerlist)
print("part1:",part1)
part2 = count_unique_answers(load_input_file2(targetfile))
print("part2:", part2)