fn main() {
    // constants
    const INPUT_FILE: &str = "../../input.txt";

    // read input into a string
    let data = std::fs::read_to_string(INPUT_FILE).unwrap();
    let data = String::from(data);
    let data = data.trim();

    // maintain the highest total calories we've seen in an inventory so far
    let mut max_cals = 0;

    // split our data into inventories and iterate over them
    for inv in data.split("\n\n") {
        // split the inventory into calories and get the total
        let mut cur_cals = 0;
        for cals in inv.split("\n") {
            let cals: u32 = cals.parse().unwrap();
            cur_cals += cals;
        }

        // check if the latest inventory is the new highest
        max_cals = std::cmp::max(max_cals, cur_cals);
    }

    // print our output to stdout
    println!("{}", max_cals);
}
