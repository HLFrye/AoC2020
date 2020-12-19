import argparse
import re

class Rule:
    def __init__(self, line):
        m1 = re.match(r"(?P<bag_type>.*) bags contain", line)
        self.type = m1.group('bag_type')
        self.sub_types = []
        idx = line.find("contain")
        end = line[idx+8:]
        if end != "no other bags.":
            contains = end.split(", ")
            for entry in contains:
                m2 = re.match(r"(?P<count>\d+) (?P<description>.+) bags?", entry)
                self.sub_types.append((int(m2.group('count')), m2.group('description')))
            

    def matches(self, bag_type):
        return bag_type in self.sub_types

class RuleBook:
    def __init__(self):
        self.rules = []

    def add_rule(self, line):
        self.rules.append(Rule(line))

    def get_opts(self, bag_type, level=0):
        print("Level {}".format(level))
        opts = set()
        for rule in self.rules:
            if rule.matches(bag_type):
                opts = set([*opts, rule.type])

        for opt in opts:
            opts = set([*opts, *self.get_opts(opt, level+1)])

        return opts

    def get_contents(self, bag_type):
        count = 1
        print(bag_type)
        for rule in self.rules:
            if rule.type == bag_type:
                print(rule.sub_types)
                for sub_type in rule.sub_types:
                    count += sub_type[0] * self.get_contents(sub_type[1])
        return count    

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", default="./sample.txt")
    args = parser.parse_args()

    rb = RuleBook()

    with open(args.input) as f:
        for line in f.readlines():
            rb.add_rule(line.strip())

    opts = rb.get_contents('shiny gold')
    print(opts)

if __name__ == '__main__':
    main()