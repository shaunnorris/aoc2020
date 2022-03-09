import pytest


test_data = ['ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:1937 iyr:2017 cid:147 hgt:183cm', 
             'iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884 hcl:#cfa07d byr:1929', 
             'hcl:#ae17e1 iyr:2013 eyr:2024 ecl:brn pid:760753108 byr:1931 hgt:179cm', 
             'hcl:#cfa07d eyr:2025 pid:166559648 iyr:2011 ecl:brn hgt:59in',
             ]

test_file = 'day4_test_input.txt'
test_file2 = 'day4_test_input2.txt'

def test_load_input_file():
    test_list = load_input_file(test_file) 
    assert len(test_list) == 4
    assert test_list == test_data
    
def load_input_file(target):
    f = open(target, 'r+')
    longline = ''
    shortlist = []
    for line in f.readlines():
        line = line.strip()
        if line != '':
            if len(longline) > 0:
                longline = longline + ' ' + line
            else:
                longline = line
        else:
            shortlist.append(longline)
            longline = ''
    f.close()
    shortlist.append(longline)
    return shortlist


def test_check_validity():
    assert check_validity(test_data) == 2


def check_validity(passport_data):
    valid_count = 0
    for passport in passport_data:
        valid = False
        entry_list = passport.split(' ')
        pp_dict = {}
        for entry in entry_list:
            keypair = entry.split(':')
            pp_dict[keypair[0]] = keypair[1]
        if len(pp_dict.keys()) == 8:
            valid = True
        elif len(pp_dict.keys()) == 7 and 'cid' not in pp_dict.keys():
            valid = True
        if valid:
            valid_count += 1
    return valid_count

"""
* byr (Birth Year) - four digits; at least 1920 and at most 2002.
* iyr (Issue Year) - four digits; at least 2010 and at most 2020.
eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
hgt (Height) - a number followed by either cm or in:
If cm, the number must be at least 150 and at most 193.
If in, the number must be at least 59 and at most 76.
hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
pid (Passport ID) - a nine-digit number, including leading zeroes.
cid (Country ID) - ignored, missing or not.
"""


@pytest.mark.parametrize("test_input,expected", [("123456789", True),("12345678", False),("1234567890", False),
                                                 ("aa", False),("99", False),("qqqq", False),("xxx", False),
                                                 ])
def test_valid_pid(test_input, expected):
    assert valid_pid(test_input) == expected

def valid_pid(pid):
    """pid (Passport ID) - a nine-digit number, including leading zeroes."""
    if len(pid) == 9:
        if pid.isnumeric():
            return True
    return False

@pytest.mark.parametrize("test_input,expected", [("amb", True),("blu", True),("brn", True),
                                                 ("gry", True),("grn", True),("hzl", True),("oth", True), 
                                                 ("aa", False),("99", False),("qqqq", False),("xxx", False),
                                                 ])
def test_valid_ecl(test_input, expected):
    assert valid_ecl(test_input) == expected


def valid_ecl(ecl):
    """ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth."""
    valid = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    if ecl in valid: 
        return True
    else:
        return False


@pytest.mark.parametrize("test_input,expected", [("#123456", True),("#789000", True),("#ABCDEF", True),
                                                 ("#G00000", False),("123456", False),("#12345", False), 
                                                 ("#1234567", False),("#ABCDEFF", False),
                                                 ])
def test_valid_hcl(test_input, expected):
    assert valid_hcl(test_input) == expected

def valid_hcl(hcl):
    valid = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','a','b','c','d','e','f']
    if hcl[0] != '#' or len(hcl) != 7:
        return False
    value =  hcl[1:]
    for char in value:
        if char not in valid: 
            return False
    return True

@pytest.mark.parametrize("test_input,expected", [("150cm", True),("193cm", True),("172cm", True),
                                                 ("59in", True),("76in", True),("65in", True), 
                                                 ("140cm", False),("205cm", False),("cm", False),
                                                 ("58in", False),("77in", False),("in", False),
                                                 ])
def test_valid_hgt(test_input, expected):
    assert valid_hgt(test_input) == expected      
 
def valid_hgt(hgt):
    '''gt (Height) - a number followed by either cm or in:
    If cm, the number must be at least 150 and at most 193.
    If in, the number must be at least 59 and at most 76.'''
    unit = hgt[-2:]
    value = hgt[:-2]
    if len(value) < 1:
        return False
    if unit == "cm":
        if 150 <= int(value) <= 193:
            return True
    if unit == 'in':
        if 59 <= int(value) <= 76:
            return True
    return False
         

@pytest.mark.parametrize("test_input,expected", [("1920", True), 
                                                 ("2002", True), 
                                                 ("1888", False),
                                                 ("22", False), 
                                                 ("19999", False),
                                                 ])
def test_valid_byr(test_input,expected):
    assert valid_byr(test_input) == expected

def valid_byr(byr):
    """byr (Birth Year) - four digits; at least 1920 and at most 2002."""
    if len(byr) == 4 and int(byr) >= 1920 and int(byr) <= 2002:
        return True
    else:
        return False

@pytest.mark.parametrize("test_input,expected", [("2010", True), 
                                                 ("2020", True), 
                                                 ("2022", False),
                                                 ("2088", False), 
                                                 ("19999", False),
                                                 ])
def test_valid_iyr(test_input, expected):
    assert valid_iyr(test_input) == expected


def valid_iyr(iyr):
    """iyr (Issue Year) - four digits; at least 2010 and at most 2020."""
    if len(iyr) == 4 and int(iyr) >= 2010 and int(iyr) <= 2020:
        return True
    else:
        return False

@pytest.mark.parametrize("test_input,expected", [("2020", True), 
                                                 ("2030", True), 
                                                 ("2032", False),
                                                 ("2018", False), 
                                                 ("19999", False),
                                                 ])
def test_valid_eyr(test_input, expected):
    assert valid_eyr(test_input) == expected

def valid_eyr(eyr):
    """eyr (Expiration Year) - four digits; at least 2020 and at most 2030."""
    if len(eyr) == 4 and int(eyr) >= 2020 and int(eyr) <= 2030:
        return True
    else:
        return False



def test_full_validity():
    test_data2 =  load_input_file(test_file2) 
    assert check_full_validity(test_data2) == 4

def check_full_validity(passport_data):
    valid_count = 0
    for passport in passport_data:
        valid = True
        ppcheck = {}
        valid_keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
        entry_list = passport.split(' ')
        pp_dict = {}
        for entry in entry_list:
            keypair = entry.split(':')
            pp_dict[keypair[0]] = keypair[1]

        keycheck = True
        for mykey in valid_keys:
            if mykey not in list(pp_dict.keys()):
                keycheck = False
            
        if keycheck:
            ppcheck['keys'] = True
            ppcheck['byr'] = valid_byr(pp_dict['byr'])
            ppcheck['iyr'] = valid_iyr(pp_dict['iyr'])
            ppcheck['eyr'] = valid_eyr(pp_dict['eyr'])
            ppcheck['hgt'] = valid_hgt(pp_dict['hgt'])
            ppcheck['hcl'] = valid_hcl(pp_dict['hcl'])
            ppcheck['ecl'] = valid_ecl(pp_dict['ecl'])
            ppcheck['pid'] = valid_pid(pp_dict['pid'])    
        else:
            ppcheck['keys'] = False

        for key, value in ppcheck.items():
            if value != True:
                valid = False
        if valid:
            valid_count += 1
    return valid_count


inputfile = 'day4input.txt'
pp_list = load_input_file(inputfile)
part1 = check_validity(pp_list)
print('part1:',part1)
part2 = check_full_validity(pp_list)
print('part2:', part2)