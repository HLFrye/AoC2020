from dataclasses import dataclass, field
from typing import Tuple

@dataclass
class Slope:
    dx: int
    dy: int

@dataclass
class Position:
    x: int
    y: int

def make_start():
    return Position(x=0, y=0)

@dataclass
class TestRun:
    slope: Slope
    pos: Position = field(default_factory=make_start)
    count: int = 0

def main():
    runs = [
        TestRun(slope=Slope(dx=1, dy=1)),
        TestRun(slope=Slope(dx=3, dy=1)),
        TestRun(slope=Slope(dx=5, dy=1)),
        TestRun(slope=Slope(dx=7, dy=1)),
        TestRun(slope=Slope(dx=1, dy=2)),
    ]
    with open("./input.txt") as f:
        for i, line in enumerate(f.readlines()):
            line = line.strip()
            for run in runs:
                if run.pos.y == i:
                    if line[run.pos.x % len(line)] == '#':
                        run.count += 1
                    run.pos.y += run.slope.dy
                    run.pos.x += run.slope.dx
    result = 1
    for run in runs:
        print(run.count)
        result *= run.count
    print(result)

if __name__ == '__main__':
    main()