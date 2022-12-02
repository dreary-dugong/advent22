#!/bin/python3
# code for https://adventofcode.com/2022/day/2 problem 2

# imports
from enum import Enum

# program constants
INPUT_FILE = "../input.txt"

# helper classes
class Move(Enum):
    """represent a move by either player in a rock paper scissors game"""

    ROCK = 1
    PAPER = 2
    SCISSORS = 3


class GameResult(Enum):
    """represent the result of a rock paper scissors game"""

    LOSS = 1
    DRAW = 2
    WIN = 3


def main():

    # function constants
    # dictionaries to decode moves and results from our input
    OPPONENT_CODES = {"A": Move.ROCK, "B": Move.PAPER, "C": Move.SCISSORS}
    RESULT_CODES = {"X": GameResult.LOSS, "Y": GameResult.DRAW, "Z": GameResult.WIN}
    # dictionaries to associate scores with player moves and game results
    MOVE_SCORES = {Move.ROCK: 1, Move.PAPER: 2, Move.SCISSORS: 3}
    RESULT_SCORES = {GameResult.LOSS: 0, GameResult.DRAW: 3, GameResult.WIN: 6}
    # dictionaries to decide the winning and losing moves to make based on the opponent's move
    WINNING_MOVES = {
        Move.ROCK: Move.PAPER,
        Move.PAPER: Move.SCISSORS,
        Move.SCISSORS: Move.ROCK,
    }
    LOSING_MOVES = {
        Move.ROCK: Move.SCISSORS,
        Move.PAPER: Move.ROCK,
        Move.SCISSORS: Move.PAPER,
    }

    # will hold the player's total score after all games, our output
    total_score = 0

    # read our input and seperate it into games
    with open(INPUT_FILE) as f:
        data = f.read().strip()
    coded_games = data.split("\n")

    # decode games and assign a score
    for game in coded_games:
        coded_op_move, coded_result = game.split(" ")
        opponent_move = OPPONENT_CODES[coded_op_move]
        result = RESULT_CODES[coded_result]

        # the portion of the score based on the game's result
        result_score = RESULT_SCORES[result]

        # get the score based on the move the player needs to make
        if result == GameResult.LOSS:
            player_move = LOSING_MOVES[opponent_move]
        elif result == GameResult.DRAW:
            player_move = opponent_move
        else:
            player_move = WINNING_MOVES[opponent_move]
        move_score = MOVE_SCORES[player_move]

        game_score = result_score + move_score
        total_score += game_score

    print(total_score)


if __name__ == "__main__":
    main()
