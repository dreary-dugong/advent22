fn main() {
    // constants
    const INPUT_FILE: &str = "../../input.txt";

    // read input into a string
    let data = std::fs::read_to_string(INPUT_FILE).unwrap();
    let data = String::from(data);
    let data = data.trim();

    // maintain a vector of the calories contained in the top 3 inventories seen so far
    let mut top3_cals: Vec<u32> = Vec::from([0, 0, 0]);

    // split our data into inventories and iterate over them
    for inv in data.split("\n\n") {
        // split the inventory into calories and get the total
        let mut cur_cals = 0;
        for cals in inv.split("\n") {
            let cals: u32 = cals.parse().unwrap();
            cur_cals += cals;
        }

        // check if the currrent inventory belongs in the top 3
        for (i, top_cals) in top3_cals.iter().enumerate() {
            // if it does, insert it and remove the one that no longer belongs
            if cur_cals > *top_cals {
                top3_cals.insert(i, cur_cals);
                top3_cals.pop();
                break;
            }
        }
    }

    // print our output to stdout
    println!("{}", top3_cals.iter().sum::<u32>());
}
