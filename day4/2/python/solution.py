#!/bin/python3
# solution for https://adventofcode.com/2022/day/4 problem 1

# program constants
INPUT_FILE = "../input.txt"


def main():

    # will contain the number of pairs with any overlap, our output
    num_overlaps = 0

    # read data from our file
    with open(INPUT_FILE) as f:
        data = f.read().strip()

    # split our data into pairs of elves and iterate
    for pair in data.split("\n"):
        # get our two ranges
        range1, range2 = pair.split(",")
        # get the  beginning and ending of each range
        start1, end1 = map(int, range1.split("-"))
        start2, end2 = map(int, range2.split("-"))

        # check for overlap
        # is the start of the second range contained in the first?
        if start2 >= start1 and start2 <= end1:
            has_overlap = True
        # is the start of the first range contained in the second?
        elif start1 >= start2 and start1 <= end2:
            has_overlap = True
        else:
            has_overlap = False

        if has_overlap:
            num_overlaps += 1

    print(num_overlaps)


if __name__ == "__main__":
    main()
