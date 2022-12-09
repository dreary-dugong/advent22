#!/bin/python3
# solution for https://adventofcode.com/2022/day/9 part 2

# helper classes
class Rope:
    """a rope (aka a linked list)"""

    def __init__(self, length, x=0, y=0):
        self.head = Knot(x=x, y=y)

        lastKnot = self.head
        for _ in range(length - 1):
            newKnot = Knot(parent=lastKnot, x=x, y=y)
            lastKnot.child = newKnot
            lastKnot = newKnot

        self.tail = lastKnot

    def move(self, direction):
        """given a direction (r, l, u, or d), move the rope one space in that direction"""
        HEAD_DELTAS = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}

        delta = HEAD_DELTAS[direction]
        self.head.x += delta[0]
        self.head.y += delta[1]

        self.head.child.follow_parent()


class Knot:
    """a knot on our rope (aka a linked list node)"""

    def __init__(self, parent=None, child=None, x=0, y=0):
        self.parent = parent
        self.child = child
        self.x = x
        self.y = y

    def follow_parent(self):
        """update the knot's position to follow a change in its parent"""
        # get relative coordinates from parent
        parent_rel_x = self.parent.x - self.x
        parent_rel_y = self.parent.y - self.y

        # figure out deltas based on relative coordinates to parent
        if parent_rel_x != 0 and (abs(parent_rel_y) == 2 or abs(parent_rel_x) == 2):
            dx = parent_rel_x // abs(parent_rel_x)
        else:
            dx = 0
        if parent_rel_y != 0 and (abs(parent_rel_y) == 2 or abs(parent_rel_x) == 2):
            dy = parent_rel_y // abs(parent_rel_y)
        else:
            dy = 0

        # apply deltas
        self.x += dx
        self.y += dy

        # trigger child to follow
        if self.child is not None:
            self.child.follow_parent()


# helper functions
def parse_input(input_file):
    """parse an input file into a series of instructions to move the snake"""
    with open(input_file) as f:
        data = f.read().strip()

    # split the input into instruction lines
    lines = data.split("\n")

    # seperate lines into their two components
    steps = []
    for line in lines:
        direction, num = line.split(" ")
        num = int(num)
        steps.append((direction, num))

    return steps


def move_rope(instructions, rope):
    """move the rope according to the given instructions and return the number of unique tail positions"""
    tail_locs = set()  # set of positions the tail has been to
    tail_coords = (rope.tail.x, rope.tail.y)  # add the starting coords
    tail_locs.add(tail_coords)

    for instruction in instructions:
        direction, num_reps = instruction
        for _ in range(num_reps):
            # move the rope and add new tail coords
            rope.move(direction)
            tail_coords = (rope.tail.x, rope.tail.y)
            tail_locs.add(tail_coords)

    return len(tail_locs)


def solve():
    """solve the problem"""
    # constants
    INPUT_FILE = "../input.txt"
    ROPE_LENGTH = 10

    instructions = parse_input(INPUT_FILE)
    rope = Rope(ROPE_LENGTH)
    num_tail_locs = move_rope(instructions, rope)

    return num_tail_locs


def main():
    print(solve())


if __name__ == "__main__":
    main()
