def main():
    buffer = None
    count = 0
    with open("./input.txt") as f:
        for line in f.readlines():
            line = line.strip()
            if buffer is None:
                buffer = set(line)
            if len(line) == 0:
                count += len(buffer)
                buffer = None
            else:
                buffer = buffer.intersection(line)
    count += len(buffer)
    print(count)

if __name__ == '__main__':
    main()