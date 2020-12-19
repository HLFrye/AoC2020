import argparse

class InvalidSequenceException(Exception):
    def __init__(self, value, block):
        self.value = value  
        super().__init__("Invalid Sequence Value {}".format(value))

class Validator:
    def __init__(self, blocksize):
        self.blocksize = blocksize
        self.block = []
        self.valid = True

    def validate(self, next):
        if len(self.block) < self.blocksize:
            self.block.append(next)
        else:
            for i in self.block:
                if (next - i) in self.block and (next - i) != i:
                    break
            else:
                raise InvalidSequenceException(next, self.block)
            self.block = [*self.block[1:], next]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    parser.add_argument("blocksize", type=int)
    args = parser.parse_args()
    validator = Validator(args.blocksize)
    with open(args.filename) as f:
        sequence = list(map(lambda x: int(x.strip()), f.readlines()))

    invalid_value = None
    try:
        for i in sequence:
            validator.validate(i)
    except InvalidSequenceException as ise:
        invalid_value = ise.value
        print("Invalid value {}, cracking...".format(invalid_value))
    
    weakness = []
    idx = 0
    test = sum(weakness)
    while test != invalid_value:
        if test < invalid_value:
            weakness.append(sequence[idx])
            idx += 1
        if test > invalid_value:
            weakness = weakness[1:]
        test = sum(weakness)
    print(min(weakness) + max(weakness))

if __name__ == '__main__':
    main()