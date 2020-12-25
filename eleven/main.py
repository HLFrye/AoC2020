import argparse

class Board:
    def __init__(self):
        self.rows = []

    def add_row(self, line):
        self.rows.append(list(line.strip()))

    def count_seats(self):
        count = 0
        for row in self.rows:
            for space in row:
                if space == '#':
                    count += 1
        return count

    def count_neighbors(self, x, y):
        count = 0
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if dx == 0 and dy == 0:
                    continue
                if (dx+x) < 0 or (dy+y) < 0 or (dx+x) >= len(self.rows[0]) or (dy+y) >= len(self.rows):
                    continue
                if self.rows[y+dy][x+dx] == '#':
                    count += 1
        return count

    def run_round(self):
        changes = []

        for y, row in enumerate(self.rows):
            for x, space in enumerate(row):
                if space == '.':
                    continue
                if space == 'L':
                    neighbors = self.count_neighbors(x, y)
                    if neighbors == 0:
                        changes.append((x, y, '#'))
                elif space == '#':
                    neighbors = self.count_neighbors(x, y)
                    if neighbors >= 4:
                        changes.append((x, y, 'L'))
        if len(changes) == 0:
            return True

        for x, y, change in changes:
            self.rows[y][x] = change
        return False

    def print(self):
        for row in self.rows:
            print("".join(row))
        print("-"*len(self.rows[0]))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()
    board = Board()
    with open(args.filename) as f:
        for line in f.readlines():
            board.add_row(line)

    count = 0
    while True:
        count += 1
        result = board.run_round()
        if result:
            break

    print(board.count_seats())

if __name__ == '__main__':
    main()