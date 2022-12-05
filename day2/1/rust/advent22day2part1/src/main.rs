enum RPSChoice {
    Rock,
    Paper,
    Scissors,
}
enum GameResult {
    Loss,
    Draw,
    Win,
}
struct RPSGame {
    opponent_choice: RPSChoice,
    player_choice: RPSChoice,
}
impl RPSGame {
    fn get_result(&self) -> GameResult {
        // return a GameResult enum representing whether the player won the game
        match self.opponent_choice {
            RPSChoice::Rock => match self.player_choice {
                RPSChoice::Rock => GameResult::Draw,
                RPSChoice::Paper => GameResult::Win,
                RPSChoice::Scissors => GameResult::Loss,
            },
            RPSChoice::Paper => match self.player_choice {
                RPSChoice::Rock => GameResult::Loss,
                RPSChoice::Paper => GameResult::Draw,
                RPSChoice::Scissors => GameResult::Win,
            },
            RPSChoice::Scissors => match self.player_choice {
                RPSChoice::Rock => GameResult::Win,
                RPSChoice::Paper => GameResult::Loss,
                RPSChoice::Scissors => GameResult::Draw,
            },
        }
    }
    fn get_score(&self) -> u32 {
        // return the game score based on the game's result and the player's choice
        let choice_score = match self.player_choice {
            RPSChoice::Rock => 1,
            RPSChoice::Paper => 2,
            RPSChoice::Scissors => 3,
        };
        let result_score = match self.get_result() {
            GameResult::Loss => 0,
            GameResult::Draw => 3,
            GameResult::Win => 6,
        };

        let total_score = choice_score + result_score;
        total_score
    }
}
fn main() {
    // imports
    use std::fs;
    // constants
    const INPUT_FILE: &str = "../../input.txt";

    // we maintain a running total of all games so far
    let mut total_score: u32 = 0;

    // read our input from a file
    let data = fs::read_to_string(INPUT_FILE).unwrap();
    let data = String::from(data);
    let data = data.trim();

    // split our input into games and iterate over them
    for line in data.split("\n") {
        // break our line into the codes for the opponent's choice and the player's choice
        let mut choices_iter = line.split(" ");
        let opponent_choice_code = choices_iter.next().unwrap();
        let player_choice_iter = choices_iter.next().unwrap();

        // decode the choices
        let opponent_choice = match opponent_choice_code {
            "A" => RPSChoice::Rock,
            "B" => RPSChoice::Paper,
            "C" => RPSChoice::Scissors,
            _ => panic!("Improper input: Expected an opponent choice of A, B, or C"),
        };
        let player_choice = match player_choice_iter {
            "X" => RPSChoice::Rock,
            "Y" => RPSChoice::Paper,
            "Z" => RPSChoice::Scissors,
            _ => panic!("Improper input: Expected a player choice of X, Y, or Z"),
        };

        // create a RPSGame struct and use it to get the score
        let game = RPSGame {
            opponent_choice,
            player_choice,
        };
        let cur_score = game.get_score();
        total_score += cur_score;
    }

    // print the total score to stdout
    println!("{}", total_score);
}
