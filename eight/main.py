import argparse
from dataclasses import dataclass, field

class Instruction:
    def __init__(self, txt):
        split = txt.split(' ')
        self.cmd = split[0]
        self.arg = int(split[1])

    def apply(self, state):
        if self.cmd == "acc":
            return ProgramState(pc=state.pc + 1, acc=state.acc + self.arg)
        elif self.cmd == "jmp":
            return ProgramState(pc=state.pc + self.arg, acc=state.acc)
        elif self.cmd == "nop":
            return ProgramState(pc=state.pc + 1, acc=state.acc)

    def swap(self):
        if self.cmd == "acc":
            return False
        if self.cmd == "jmp":
            self.cmd = "nop"
            return True
        if self.cmd == "nop":
            self.cmd = "jmp"
            return True

@dataclass
class ProgramState:
    pc: int = field(default=0)
    acc: int = field(default=0)

class Executor:
    def __init__(self):
        self.state = ProgramState()

    def execute(self, program):
        visits = {}
        while self.state.pc not in visits:
            if self.state.pc == len(program):
                return True, self.state.acc
            visits[self.state.pc] = self.state.acc
            instruction = program[self.state.pc]
            self.state = instruction.apply(self.state)

        return False, self.state.acc

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", default="./sample.txt")
    args = parser.parse_args()
    program = []
    with open(args.filename) as f:
        for line in f.readlines():
            program.append(Instruction(line.strip()))

    for i in range(0, len(program)):
        if (program[i].swap()):
            executor = Executor()
            success, acc = executor.execute(program)
            if success:
                print(acc)
                return
            program[i].swap()

if __name__ == '__main__':
    main()