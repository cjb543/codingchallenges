use std::fs;

fn main() -> Result<(), Box<dyn std::error::Error>> {
    // Assign file data to "data" variables
    let data = read_file_string("../input.txt")?;

    // Solution 1
    let mut counter = 0;
    for c in data.chars(){
        if c == '(' { counter += 1; }
        else if c == ')' { counter -= 1; }
    }
    println!("Part 1 Solution: {}",counter);

    // Solution 2
    let mut floor = 0; counter = 0;
    let mut basement_floors = Vec::new();
    for c in data.chars(){
        if c == '(' { floor += 1; counter += 1; }
        if c == ')' { floor -= 1; counter += 1; }
        if floor == -1 { basement_floors.push(counter);}
    }
    println!("Part 2 Solution: {}", basement_floors[0]);

    Ok(())
}

// Reads a file to a returned string
fn read_file_string(filepath: &str) -> Result<String, Box<dyn std::error::Error>>{
    let data = fs::read_to_string(filepath)?;
    Ok(data)
}
