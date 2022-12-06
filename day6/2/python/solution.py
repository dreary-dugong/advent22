#!/bin/python3
# solution for https://adventofcode.com/2022/day/6 part 1
# program constants
INPUT_FILE = "../input.txt"
MARKER_SIZE = 14


def main():
    # read data from file
    with open(INPUT_FILE) as f:
        message = f.read().strip()

    # use two pointers to move a sliding window
    left = 0
    right = left + MARKER_SIZE
    seen = (
        dict()
    )  # store the characters we've seen in the window so far with an index so we can go back to them if needed

    found_marker = False
    while not found_marker:

        # progress the left side until it's a dupe or meets the right
        while left < right and message[left] not in seen:
            seen[message[left]] = left
            left += 1

        # if left and right are the same, we found our marker
        if left == right:
            found_marker = True
            marker_end = left - 1
        # otherwise, we'll need to move the window along just after the first instance of the repeated character and try again
        else:
            left = seen[message[left]] + 1
            right = left + MARKER_SIZE
            seen.clear()

    # output the number of characters proccessed
    print(marker_end + 1)


if __name__ == "__main__":
    main()
