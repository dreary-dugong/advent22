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
    forest = [list(map(int, line)) for line in char_lists]

    return forest


def rotate_matrix_left(matrix):
    """given a 2d matrix, rotate it 90 degrees to the left"""
    ncols = len(matrix[0])
    rev_cols = []
    for i in range(ncols - 1, -1, -1):
        col = [row[i] for row in matrix]
        rev_cols.append(col)
    return rev_cols


def rotate_matrix_right(matrix):
    """given a 2d matrix, rotate it 90 degrees to the right"""
    ncols = len(matrix[0])
    rev_cols = []
    for i in range(ncols):
        col = [row[i] for row in matrix[::-1]]
        rev_cols.append(col)
    return rev_cols


def get_direction_scores(forest):
    """given a forest, return the left component of the visibility score"""
    nrows = len(forest)
    ncols = len(forest[0])
    scores = [[0] * ncols for _ in range(nrows)]

    for row_index in range(nrows):
        for col_index in range(ncols):

            cur_score = 0
            if col_index != 0:
                cur_height = forest[row_index][col_index]
                for col_pointer in range(col_index - 1, -1, -1):
                    cur_score += 1
                    if forest[row_index][col_pointer] >= cur_height:
                        break

            scores[row_index][col_index] = cur_score

    return scores


def old_get_direction_scores(forest):
    """given a forest, return the left component of the visibility score"""
    nrows = len(forest)
    ncols = len(forest[0])

    # matrix  of scores we've found so far to speed up finding the next one
    scores = [[0 for _ in range(ncols)] for _ in range(nrows)]
    for row_index in range(nrows):
        for col_index in range(ncols):

            if col_index == 0:
                cur_score = 0
            else:
                cur_height = forest[row_index][col_index]
                neighbor_height = forest[row_index][col_index - 1]
                if neighbor_height >= cur_height:
                    cur_score = 1
                else:
                    neighbor_score = scores[row_index][col_index - 1]
                    cur_score = neighbor_score + 1

            scores[row_index][col_index] = cur_score

    return scores


def get_best_tree(north_scores, east_scores, south_scores, west_scores):
    nrows = len(north_scores)
    ncols = len(north_scores[0])
    best_score = 0
    for row_index in range(nrows):
        for col_index in range(ncols):
            north = north_scores[row_index][col_index]
            east = east_scores[row_index][col_index]
            south = south_scores[row_index][col_index]
            west = west_scores[row_index][col_index]

            cur_score = north * east * south * west
            best_score = max(best_score, cur_score)

    return best_score


def solve():
    """solve the problem"""
    # constants
    INPUT_FILE = "../input.txt"

    forest = parse_input(INPUT_FILE)

    # we use dp to find the visibility score in a single direction
    west_scores = get_direction_scores(forest)

    # then we rotate the forest and do it again
    south_forest = rotate_matrix_right(forest)
    south_scores = get_direction_scores(south_forest)
    # rotate the scores back so the coords match
    south_scores = rotate_matrix_left(south_scores)

    # repeat for west but rotate back twice
    # could use a function to rotate 180 instead and save time
    east_forest = rotate_matrix_right(south_forest)
    east_scores = get_direction_scores(east_forest)
    east_scores = rotate_matrix_left(rotate_matrix_left(east_scores))

    # repeat for north but rotate once more around
    north_forest = rotate_matrix_right(east_forest)
    north_scores = get_direction_scores(north_forest)
    north_scores = rotate_matrix_right(north_scores)

    return get_best_tree(north_scores, east_scores, south_scores, west_scores)


def main():
    print(solve())


def pretty_print_matrix(matrix):
    print("[")
    for row in matrix:
        print(row)
    print("]")


if __name__ == "__main__":
    main()
