fn main() {
    // imports
    use std::fs;
    // constants
    const INPUT_FILE: &str = "../../input.txt";
    // read input
    let data = fs::read_to_string(INPUT_FILE).expect("Error: Missing input file.");
    let data = data.trim();

    // the number of pairs in which one range contains the other, our output
    let mut num_containing_pairs = 0;

    // iterate over lines in our input representing pairs of elves
    for pair_line in data.split("\n") {
        let mut elves = pair_line.split(","); // seperate the line into two elves
        let mut elf1 = elves.next().unwrap().split("-");
        let mut elf2 = elves.next().unwrap().split("-");
        let elf1_start = elf1.next().unwrap().parse::<u32>().unwrap();
        let elf1_end = elf1.next().unwrap().parse::<u32>().unwrap();
        let elf2_start = elf2.next().unwrap().parse::<u32>().unwrap();
        let elf2_end = elf2.next().unwrap().parse::<u32>().unwrap();

        // check if either range overlaps with the other
        if elf1_start <= elf2_start && elf2_start <= elf1_end {
            num_containing_pairs += 1;
        } else if elf2_start <= elf1_start && elf1_start <= elf2_end {
            num_containing_pairs += 1;
        }
    }

    // print our answer to stdout
    println!("{}", num_containing_pairs)
}
