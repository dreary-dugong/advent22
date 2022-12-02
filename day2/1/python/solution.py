#!/bin/python3
# code for https://adventofcode.com/2022/day/2 problem 1

# program constants
INPUT_FILE = "../input.txt"


def main():

    # function constants
    # dictionaries to decode moves from our input
    OPPONENT_CODES = {"A": "rock", "B": "paper", "C": "scissors"}
    PLAYER_CODES = {"X": "rock", "Y": "paper", "Z": "scissors"}
    # dictionary to associate a score with a player move
    MOVE_SCORES = {"rock": 1, "paper": 2, "scissors": 3}
    # tuples of opponent's move, player's move in which the player wins
    WINNING_GAMES = (("rock", "paper"), ("scissors", "rock"), ("paper", "scissors"))

    # will hold the player's total score after all games, our output
    total_score = 0

    # read our input and seperate it into games
    with open(INPUT_FILE) as f:
        data = f.read().strip()
    coded_games = data.split("\n")

    # decode games and assign a score
    for game in coded_games:
        coded_op_move, coded_player_move = game.split(" ")
        opponent_move = OPPONENT_CODES[coded_op_move]
        player_move = PLAYER_CODES[coded_player_move]

        # the portion of the score based on the player's move
        move_score = MOVE_SCORES[player_move]

        # get the result portion of the score
        # draw
        if opponent_move == player_move:
            result_score = 3
        # win
        elif (opponent_move, player_move) in WINNING_GAMES:
            result_score = 6
        # otherwise, it must be a loss
        else:
            result_score = 0

        game_score = move_score + result_score
        total_score += game_score

    print(total_score)


if __name__ == "__main__":
    main()
