
def main():
    entries = {}
    with open("./input.txt") as f:
        for line in f.readlines():
            num = int(line)
            for key, value in entries.items():
                if num in value:
                    print("{} * {} * {} = {}".format(num, key, value[num], num*key*value[num]))
                    return
                value[2020-key-num] = num
            entries[num] = {}

if __name__ == '__main__':
    main()