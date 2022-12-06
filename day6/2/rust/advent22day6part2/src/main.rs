fn main() {
    // constants
    const INPUT_FILE: &str = "../../input.txt";
    const MARKER_LENGTH: usize = 14;
    // imports
    use std::collections::HashMap;
    use std::fs;

    // read data from file
    let data = fs::read_to_string(INPUT_FILE).expect("Error: missing input file");
    let data = data.trim();
    let transmission = data.as_bytes();

    // maintain a sliding window the same length as the marker length
    let mut found_marker = false;
    let mut left: usize = 0;
    let mut right: usize = left + MARKER_LENGTH;
    // a hashmap of characters seen in the window and where they were
    let mut seen: HashMap<u8, usize> = HashMap::with_capacity(MARKER_LENGTH);

    while !found_marker {
        // progress the left pointer forward, checking for repeat characters
        while left < right && !seen.contains_key(&transmission[left]) {
            seen.insert(transmission[left], left);
            left += 1;
        }
        // if we make it all the way to the right without repeats, we found the marker
        if left == right {
            found_marker = true;
        // otherwise, move the right side forward and set left to last repeated character
        } else {
            left = *seen.get(&transmission[left]).unwrap() + 1;
            right = left + MARKER_LENGTH;
            seen.clear();
        }
    }

    // print the number of characters processed to stdout
    println!("{}", left);
}
