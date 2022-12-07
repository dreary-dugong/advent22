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
    const GROUP_SIZE: usize = 3;

    // read data from file
    let data = fs::read_to_string(INPUT_FILE).expect("Error: Missing input file.");
    let data = data.trim();

    // keep track of the total score for all badges so far, our output
    let mut total_score: u32 = 0;

    // iterate over groups of 3 rucksacks
    let lines: Vec<&str> = data.split("\n").collect();
    for group in lines.chunks(GROUP_SIZE) {
        let mut group_iter = group.iter();
        // initialize possible badges with all items in first rucksack
        let mut possible_badges: HashSet<&u8> =
            HashSet::from_iter(group_iter.next().unwrap().as_bytes());

        // iterate over remaining rucksack and replace the hashset with a subset that's in every rucksack so far
        for rucksack in group_iter {
            let mut new_possible_badges: HashSet<&u8> = HashSet::new();
            for item in rucksack.as_bytes() {
                if possible_badges.contains(item) {
                    new_possible_badges.insert(item);
                }
            }
            possible_badges = new_possible_badges;
        }

        let badge = possible_badges.iter().next().unwrap();
        let cur_score = get_score(**badge);
        total_score += cur_score;
    }
    // print the total score to stdout
    println!("{}", total_score);
}
