from functools import partial

def part1_validate(min, max, key, test):
    occs = test.count(key)
    if occs >= min and occs <= max:
        return True

# 257 is too low?

def validate(p1, p2, key, test):
    isValid = 0
    if test[p1-1] == key:
        isValid += 1
    if test[p2-1] == key:
        isValid += 1
    if isValid != 1:
        print("{}-{} {}: {}".format(p1, p2, key, test))
    return isValid == 1

def validatorbuilder(rule):
    counts, key = rule.split(" ")
    keyMin, keyMax = [int(x) for x in counts.split("-")]
    return partial(validate, keyMin, keyMax, key)

def main():
    count = 0
    validators={}
    with open("./input.txt") as f:
        for line in f.readlines():
            rule, test = line.split(": ")
            test = test.strip()
            if rule not in validators:
                validators[rule] = validatorbuilder(rule)
            validator = validators[rule]
            if validator(test):
                count = count + 1
    print(count)

if __name__ == '__main__':
    main()