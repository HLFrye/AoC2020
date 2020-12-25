import argparse

paths = {
    1: 1,
    2: 1,
    3: 2,
    4: 4,
    5: 7,
}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()
    values = [0]
    with open(args.filename) as f:
        for line in f.readlines():
            value = int(line)
            values.append(value)

    values.sort()
    segments = [[values[0]]]
    curr_segment = 0
    differences = {}
    for value, next_value in zip(values, values[1:]):
        diff = next_value - value
        if diff == 3:
            curr_segment+=1
            segments.append([next_value])
        else:
            segments[curr_segment].append(next_value)
        old_count = differences.get(diff, 0)
        differences[diff] = old_count + 1
    differences[3] += 1
    print(differences)
    print(differences[1] * differences[3])

    path_count = 1

    print("{} segments".format(len(segments)))
    for seg in segments:
        print(len(seg))
        path_count = path_count * paths[len(seg)]

    print(path_count)

if __name__ == '__main__':
    main()