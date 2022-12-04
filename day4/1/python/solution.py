#!/bin/python3
# solution for https://adventofcode.com/2022/day/4 problem 1

# program constants
INPUT_FILE = "../input.txt"


def main():

    # will contain the number of pairs where one fully overlaps the other, our output
    num_fully_overlapping_pairs = 0

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

        # check if the second range is inside the first
        if start2 >= start1 and end2 <= end1:
            does_pair_overlap = True
        # if the first pair is inside the second
        elif start1 >= start2 and end1 <= end2:
            does_pair_overlap = True
        # otherwise, there's no overlap
        else:
            does_pair_overlap = False

        if does_pair_overlap:
            num_fully_overlapping_pairs += 1

    print(num_fully_overlapping_pairs)


if __name__ == "__main__":
    main()
