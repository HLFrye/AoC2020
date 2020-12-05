def main():
    highest = 0
    all_seats = { val: True for val in range(0, 0b1111111111) }
    with open ("./input.txt") as f:
        for line in f.readlines():
            line = line.strip()
            original = line
            line = line.replace('L', '0')
            line = line.replace('R', '1')
            line = line.replace('F', '0')
            line = line.replace('B', '1')
            value = int(line, 2)
            print("{} = {}".format(line, value))
            if value > highest:
                highest = value
            del(all_seats[value])

    print(highest)
    for val in all_seats.keys():
        print(val)

if __name__ == '__main__':
    main()