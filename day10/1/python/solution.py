#!/bin/python3
# solution for https://adventofcode.com/2022/day/10 part 1

# helper classes
class Device:
    # the number of cycles  needed to complete each instruction
    CYCLE_COUNTS = {"noop": 1, "addx": 2}

    def __init__(self, mem):
        # set the memory to the instructions
        self.mem = mem
        # set the execution pointer to the beginning of memory
        self.exec_pointer = 0
        # set registers to inital values
        self.x = 1
        # the number of cycles remaining on the current instruction
        self.remaining_inst_cycles = Device.CYCLE_COUNTS[self.mem[self.exec_pointer][0]]
        # the total number of cycles used so far
        self.num_cycles = 0
        # is the device out of instructions to execute
        self.halt = len(self.mem) == 0
        # what was the x register during the last cycle
        # this is a bit of a hack but the problem is stupid for asking for this
        self.x_during_last = self.x

    def exec_noop(self, args):
        """execute the noop instruction aka do nothing"""
        pass

    def exec_addx(self, args):
        """execute the addx instruction aka add a value to x"""
        v = int(args[0])
        self.x += v

    def exec(self, inst):
        """execute a given instruction"""
        INST_FUNCS = {"noop": self.exec_noop, "addx": self.exec_addx}
        inst_code, args = inst[0], inst[1:]
        inst_func = INST_FUNCS[inst_code]
        inst_func(args)

    def cycle(self):
        """cycle the device one time"""
        # update the hacky "what was x during the previous cycle" variable
        self.during_last = self.x

        # if we're halted, stay halted
        if self.halt:
            return

        current_inst = self.mem[self.exec_pointer]
        self.remaining_inst_cycles -= 1

        # if we've waited all the cycles we need to in order to execute the instruction
        if self.remaining_inst_cycles == 0:
            self.exec(current_inst)

            # prep for next instruction
            self.exec_pointer += 1
            if self.exec_pointer < len(self.mem):
                current_inst = self.mem[self.exec_pointer]
                inst_code = current_inst[0]
                self.remaining_inst_cycles = Device.CYCLE_COUNTS[inst_code]
            else:
                self.halt = True

        self.num_cycles += 1

    def get_signal_strength(self):
        """return the signal strenth of the current state"""
        return self.during_last * self.num_cycles


def parse_input(input_file):
    """parse the input file into a list of instructions"""
    with open(input_file) as f:
        data = f.read().strip()
    lines = data.split("\n")
    instructions = [line.split(" ") for line in lines]
    return instructions


def solve():
    """solve the problem"""
    # constants
    INPUT_FILE = "../input.txt"

    instructions = parse_input(INPUT_FILE)
    device = Device(instructions)
    ss_sum = 0  # the sum of all the signal strengths recorded so far

    # cycle the device until it can't anymore
    while not device.halt:
        device.cycle()
        if (device.num_cycles % 40) - 20 == 0:
            ss_sum += device.get_signal_strength()

    return ss_sum


def main():
    print(solve())


if __name__ == "__main__":
    main()
