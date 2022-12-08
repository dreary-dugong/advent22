#!/bin/python3
# solution for https://adventofcode.com/2022/day/8/input part 1

# imports
from collections import defaultdict


def parse_input(input_file):
    """take our input file and output it as a matrix of ints"""
    with open(input_file) as f:
        data = f.read().strip()
    lines = data.split("\n")  # seperate into lines
    char_lists = map(list, lines)  # seperate lines into characters
    # make the characters into ints
    trees = [list(map(int, line)) for line in char_lists]

    return trees


def count_visible(trees):
    """given rows and columns of our forest, count the visible trees"""
    nrows = len(trees)
    ncols = len(trees[0])
    # keep track of the tallest trees we've seen per row and column to
    # make it faster to tell if a tree is visible from the north or west
    highest_tree_per_row = defaultdict(lambda: 0)
    highest_tree_per_col = defaultdict(lambda: 0)
    # iterate over every tree and check if it's visible
    num_visible = 0
    for row_index in range(nrows):
        for col_index in range(ncols):
            highest_in_row = highest_tree_per_row[row_index]
            highest_in_col = highest_tree_per_col[col_index]
            cur_height = trees[row_index][col_index]
            visible = False

            # check if the tree is on an edge
            if (
                row_index == 0
                or row_index == nrows - 1
                or col_index == 0
                or col_index == ncols - 1
            ):
                visible = True

            # check from the north
            if not visible and cur_height > highest_in_col:
                visible = True

            # check from the west
            if not visible and cur_height > highest_in_row:
                visible = True

            # check from the east
            if not visible:
                row_pointer = row_index + 1
                # look through all the trees to the right. If one is higher, we move on
                while (
                    row_pointer < nrows and trees[row_pointer][col_index] < cur_height
                ):
                    row_pointer += 1
                # if the loop finished without finding a higher tree, it's visible
                if row_pointer == nrows:
                    visible = True

            # check from the south
            if not visible:
                col_pointer = col_index + 1
                # look through all the trees below. If one is higher, we move on
                while (
                    col_pointer < ncols and trees[row_index][col_pointer] < cur_height
                ):
                    col_pointer += 1
                # if the loop finished without finding a higher tree, it's visible
                if col_pointer == ncols:
                    visible = True

            # we now know if the tree is visibl3
            # update our highest trees
            highest_tree_per_row[row_index] = max(cur_height, highest_in_row)
            highest_tree_per_col[col_index] = max(cur_height, highest_in_col)

            if visible:
                num_visible += 1

    return num_visible


def solve():
    """solve the problem"""
    # constants
    INPUT_FILE = "../input.txt"

    trees = parse_input(INPUT_FILE)
    num_visible = count_visible(trees)

    return num_visible


def main():
    print(solve())


if __name__ == "__main__":
    main()
