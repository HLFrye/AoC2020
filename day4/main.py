from functools import partial
import re

required_fields = [
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid",
]

optional_fields = [
    "cid",
]

def parse_passport(text_input):
    text_input = text_input.split()
    text_input = map(lambda x: tuple(x.split(':')), text_input)
    text_input = {key: value for key, value in text_input}
    return text_input

def validate_year(min, max, value):
    value = int(value)
    return value >= min and value <= max

def validate_height(input):
    if input.endswith("cm"):
        value = int(input[:-2])
        return value >= 150 and value <= 193
    if input.endswith("in"):
        value = int(input[:-2])
        return value >= 59 and value <= 76
    return False 

def validate_hair(input):
    return re.match(r"^#[0-9a-f]{6}$", input, re.RegexFlag.IGNORECASE)    

def validate_eye(input):
    return input in [
        'amb',
        'blu',
        'brn',
        'gry',
        'grn',
        'hzl',
        'oth',
    ]

def validate_pid(input):
    return re.match(r"^\d{9}$", input)

def validate_cid(input):
    return True

validators = {
    'byr': partial(validate_year, 1920, 2002),
    'iyr': partial(validate_year, 2010, 2020),
    'eyr': partial(validate_year, 2020, 2030),
    'hgt': validate_height,
    'hcl': validate_hair,
    'ecl': validate_eye,
    'pid': validate_pid,
    'cid': validate_cid,
}

def validate_passport(text_input):
    passport = parse_passport(text_input)
    requirements_met = 0
    optionals_found = 0
    for key, value in passport.items():
        if key in required_fields:
            requirements_met += 1
        if not validators[key](value):
            return False
    return requirements_met == len(required_fields)

def main():
    buffer = ""
    count = 0
    with open("./input.txt") as f:
        for line in f.readlines():
            if len(line.strip()) == 0:
                if validate_passport(buffer):
                    count += 1
                buffer = ""
            else:
                buffer = " ".join([buffer, line.strip()])

        if validate_passport(buffer):
            count += 1
    print(count)

if __name__ == '__main__':
    main()