fn get_score(item: u8) -> u32 {
    // return the score of an item based on its character code
    // uppercase characters
    if ('A' as u8) <= item && item <= ('Z' as u8) {
        (item - ('A' as u8) + 1 + 26) as u32
    // lowercase characters
    } else if ('a' as u8) <= item && item <= ('z' as u8) {
        (item - ('a' as u8) + 1) as u32
    // invalid characters
    } else {
        panic!("Invalid item character");
    }
}
fn main() {
    // imports
    use std::collections::HashSet;
    use std::fs;
    // constants
    const INPUT_FILE: &str = "../../input.txt";

    // read data from file
    let data = fs::read_to_string(INPUT_FILE).expect("Error: Missing input file.");
    let data = data.trim();

    // keep track of the total score for all rucksacks so far, our output
    let mut total_score: u32 = 0;

    // iterate over rucksacks line by line
    for rucksack in data.split("\n") {
        // split the rucksack into two halves and hash the first for efficient lookup
        let items = rucksack.as_bytes();
        let first_half = &items[..items.len() / 2];
        let second_half = &items[items.len() / 2..];
        let first_half_set: HashSet<&u8> = HashSet::from_iter(first_half);

        // iterate over characters in the second half until we find the one in the first half
        for item in second_half {
            if first_half_set.contains(item) {
                // once we find it, add to our total score and exit
                total_score += get_score(*item);
                break;
            }
        }
    }
    // print the total score to stdout
    println!("{}", total_score);
}
