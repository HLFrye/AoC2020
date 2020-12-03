from functools import partial

def validate(min, max, key, test):
    occs = test.count(key)
    if occs >= min and occs <= max:
        return True

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
            if rule not in validators:
                validators[rule] = validatorbuilder(rule)
            validator = validators[rule]
            if validator(test):
                count = count + 1
    print(count)

if __name__ == '__main__':
    main()