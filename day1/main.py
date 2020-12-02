
def main():
    entries = {}
    with open("./input.txt") as f:
        for line in f.readlines():
            num = int(line)
            pair = 2020 - num
            if pair in entries:
                print("{} * {} = {}".format(num, pair, num*pair))
                return
            entries[num] = 1
            
if __name__ == '__main__':
    main()