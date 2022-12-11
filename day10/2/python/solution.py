#!/bin/python3
# solution for https://adventofcode.com/2022/day/10 part 2

# helper classes
class Device:
    """the cpu in our device that executes instructions"""

    # the number of cycles  needed to complete each instruction
    CYCLE_COUNTS = {"noop": 1, "addx": 2}
    # constants for the crt
    LIT_PIXEL = "#"
    DARK_PIXEL = "."
    CRT_WIDTH = 40

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
        # the screen on the device
        self.crt = [[]]

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
        # if we're halted, stay halted
        if self.halt:
            return

        # update screen
        self.draw_pixel()

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

    def draw_pixel(self):
        """add a pixel to the screen based on the x register"""
        cur_row = self.crt[-1]
        cursor = len(cur_row)
        if self.x - 1 <= cursor <= self.x + 1:
            cur_row.append(Device.LIT_PIXEL)
        else:
            cur_row.append(Device.DARK_PIXEL)

        if len(cur_row) == Device.CRT_WIDTH:
            self.crt.append([])

    def run(self):
        """execute instructions until we can't"""
        while not self.halt:
            self.cycle()

    def get_screen(self):
        """return the contents of the crt as a string"""
        out = []
        for row in self.crt:
            out.append("".join(row))
            out.append("\n")
        return "".join(out)


# helper functions
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
    device.run()
    screen = device.get_screen()

    return screen


def main():
    print(solve())


if __name__ == "__main__":
    main()
