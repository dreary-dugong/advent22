#!/bin/python3
# solution for https://adventofcode.com/2022/day/3 problem 1

# program constants
INPUT_FILE = "../input.txt"

# helper functions
def get_priority(item):
    """return the 'priority' number of a given item, represented by a letter"""
    ascii_code = ord(item)
    # if it's lowercase
    if ascii_code >= ord("a"):
        return ascii_code - (ord("a") - 1)
    # if it's uppercase
    return ascii_code - (ord("A") - 1) + 26


def main():

    # the total priority of all misplaced items in all rucksacks, our output
    total_priority = 0

    # read our data from our file
    with open(INPUT_FILE) as f:
        data = f.read().strip()

    # seperate into rucksacks and iterate over them
    rucksacks = data.split("\n")
    for rucksack in rucksacks:

        # seperate into our two compartments
        first_compartment = rucksack[: len(rucksack) // 2]
        second_compartment = rucksack[len(rucksack) // 2 :]

        # put items from first compartment in a hash set
        first_compartment_set = set(first_compartment)

        # check if each item from the second compartment is in the first
        for item in second_compartment:
            if item in first_compartment_set:
                dupe = item
                break

        cur_priority = get_priority(dupe)
        total_priority += cur_priority

    print(total_priority)


if __name__ == "__main__":
    main()
