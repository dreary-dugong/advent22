#!/bin/python3
# solution for https://adventofcode.com/2022/day/9 part 1


def parse_input(input_file):
    """parse an input file into a series of instructions to move the snake"""
    with open(input_file) as f:
        data = f.read().strip()
    lines = data.split("\n")
    steps = []
    for line in lines:
        direction, num = line.split(" ")
        num = int(num)
        steps.append((direction, num))
    return steps


def move_snake(instructions):
    """move the head and tail according to a list of instructions and
    return the number of unique tail positions"""
    head_coords = [0, 0]
    tail_coords = [0, 0]
    # dictionary of how to move the head given a direction
    head_deltas = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}
    # set of locations where the tail has been
    tail_visited = set()
    tail_visited.add((0, 0))

    for instruction in instructions:
        direction, num_steps = instruction
        head_dx, head_dy = head_deltas[direction]
        for _ in range(num_steps):
            # move head
            head_coords[0] += head_dx
            head_coords[1] += head_dy

            # use relative coordinates of the tail to the head to get the tail delta
            tail_rel_x = head_coords[0] - tail_coords[0]
            tail_rel_y = head_coords[1] - tail_coords[1]

            if tail_rel_x != 0 and (abs(tail_rel_y) == 2 or abs(tail_rel_x) == 2):
                tail_dx = tail_rel_x // abs(tail_rel_x)
            else:
                tail_dx = 0

            if tail_rel_y != 0 and (abs(tail_rel_y) == 2 or abs(tail_rel_x) == 2):
                tail_dy = tail_rel_y // abs(tail_rel_y)
            else:
                tail_dy = 0

            # move tail
            tail_coords[0] += tail_dx
            tail_coords[1] += tail_dy
            tail_visited.add(tuple(tail_coords))

    return len(tail_visited)


def print_grid(head_coords, tail_coords):
    """print the snake's position just like the prompt for debugging"""
    print("\n")
    for y in range(4, -1, -1):
        line = []
        for x in range(0, 6):
            if head_coords == [x, y]:
                line.append("H")
            elif tail_coords == [x, y]:
                line.append("T")
            else:
                line.append(".")
        print("".join(line))


def solve():
    """solve the problem"""
    # constants
    INPUT_FILE = "../input.txt"

    instructions = parse_input(INPUT_FILE)
    num_tail_locs = move_snake(instructions)

    return num_tail_locs


def main():
    print(solve())


if __name__ == "__main__":
    main()
