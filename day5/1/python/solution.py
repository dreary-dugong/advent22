#!/bin/python3
# solution for https://adventofcode.com/2022/day/5 part 1

# program constants
INPUT_FILE = "../input.txt"


def main():

    # read data from input file
    with open(INPUT_FILE) as f:
        data = f.read().strip()

    # seperate our data into its discrete categories
    chart, instructions = data.split("\n\n")
    chart_lines = chart.split("\n")
    chart_labels = chart_lines[-1]
    chart_data = chart_lines[:-1]

    # create our stacks based on our input
    # we assume the number of stacks is <=9. If it were greater than 9, the known input format wouldn't work.
    num_stacks = int(chart_labels.strip()[-1])
    stacks = [[] for _ in range(num_stacks)]

    # go through the chart from the bottom up and add crates to our stacks
    for line in chart_data[::-1]:
        for i, stack in enumerate(stacks):
            stack_index = (
                1 + 4 * i
            )  # the index on the line where the letters should be for the current stack
            if stack_index < len(line) and line[stack_index] != " ":
                stack.append(line[stack_index])

    # execute the listed instructions
    for instruction in instructions.split("\n"):

        # extract the numbers we need from the instruction
        tokens = instruction.strip().split(" ")
        num_crates = int(tokens[1])
        starting_stack_index = int(tokens[3]) - 1
        ending_stack_index = int(tokens[5]) - 1

        # move crates according to the numbers
        starting_stack = stacks[starting_stack_index]
        ending_stack = stacks[ending_stack_index]
        for _ in range(num_crates):
            cur_crate = starting_stack.pop()
            ending_stack.append(cur_crate)

    # get our output: the top crate on every stack
    print("".join([stack[-1] for stack in stacks]))


if __name__ == "__main__":
    main()
