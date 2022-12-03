#!/bin/python3
# solution for https://adventofcode.com/2022/day/3 problem 2

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

    # function constants
    GROUP_SIZE = 3  # the number of elves in a group

    # the total priority of all group badges, our output
    total_priority = 0

    # read our data from our file
    with open(INPUT_FILE) as f:
        data = f.read().strip()

    # seperate rucksacks into groups
    rucksacks = data.split("\n")
    groups = []
    curGroup = []
    for rucksack in rucksacks:
        curGroup.append(rucksack)

        if len(curGroup) == GROUP_SIZE:
            groups.append(curGroup)
            curGroup = []

    # iterate over our groups and find their badges
    for group in groups:

        # we maintain a hashset of every item seen in all rucksacks so far
        possible_badges = set(group[0])

        for i, rucksack in enumerate(group[1:]):
            # we construct a second hash set which is a subset of the first, reduced to those shared by the current rucksack
            new_possible_badges = set()
            for item in rucksack:
                # if we're on the last rucksack and we have a badge, exit (this isn't necessary, but might save some time)
                if i == len(group) - 2 and item in possible_badges:
                    badge = item
                    break
                # otherwise if we have an item in possible badges, we add it to our new set
                elif item in possible_badges:
                    new_possible_badges.add(item)

            # update possible badges to the new reduced subset
            possible_badges = new_possible_badges

        badge_priority = get_priority(badge)
        total_priority += badge_priority

    print(total_priority)


if __name__ == "__main__":
    main()
