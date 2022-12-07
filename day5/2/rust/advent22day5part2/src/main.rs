fn main() {
    // imports
    use std::fs;
    // constants
    const INPUT_FILE: &str = "../../input.txt";

    // read data from our file
    let data = fs::read_to_string(INPUT_FILE).expect("Error: Missing input file.");
    let data = data.trim_end();

    // seperate our data into the chart and the instructions
    let mut sections = data.split("\n\n");
    let chart = sections.next().unwrap();
    let instructions = sections.next().unwrap().trim();

    // seperate the chart into lines and process them in reverse
    let mut chart_lines = chart.split("\n").collect::<Vec<&str>>();
    chart_lines.reverse();
    let mut rev_chart_iter = chart_lines.iter();

    // create our stacks and populate them according to the chart
    let stack_labels = rev_chart_iter.next().unwrap().trim();
    let num_stacks = *stack_labels.as_bytes().last().unwrap();
    let num_stacks = (num_stacks - ('1' as u8 - 1)) as usize; // convert from ascii code
    let mut stacks: Vec<Vec<u8>> = vec![Vec::new(); num_stacks];
    for line in rev_chart_iter {
        let line_bytes = line.as_bytes();
        for stack_num in 0..num_stacks {
            let line_index = 1 + 4 * stack_num; // the location of the stack on the line

            // bounds check
            if line_index < line_bytes.len() {
                let line_char = line_bytes[line_index];
                // ignore spaces
                if line_char != (' ' as u8) {
                    stacks[stack_num].push(line_bytes[line_index]);
                }
            }
        }
    }

    // iterate over the instructions and follow them
    for instruction in instructions.split("\n") {
        let tokens: Vec<_> = instruction.split(" ").collect();
        let num_crates: usize = tokens[1].parse().unwrap();
        let source_stack_num = tokens[3].parse::<usize>().unwrap() - 1;
        let dest_stack_num = tokens[5].parse::<usize>().unwrap() - 1;

        // drain the given number of crates from our source and append them to our destination
        let source_stack = &mut stacks[source_stack_num];
        let mut transit_crates: Vec<_> = source_stack
            .drain(source_stack.len() - num_crates..)
            .collect();
        let dest_stack = &mut stacks[dest_stack_num];
        dest_stack.append(&mut transit_crates);
    }

    // get the top crate from every stack
    let top_crates: String = stacks
        .iter()
        .map(|stack| *(stack.last().unwrap()) as char)
        .collect();

    // print to stdout
    println!("{:?}", top_crates);
}
