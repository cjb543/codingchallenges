use std::fs::File;
use std::io::{self, prelude::*, BufReader};
use std::cmp;
fn main() -> io::Result<()>{

    // Open a file and read buffer into "reader" (better approach than day 1)
    let file = File::open("../input.txt")?;
    let reader = BufReader::new(file);
    let mut total_surface_area = 0;


    // Solution 1
    for line_result in reader.lines(){
        // Separate lines into 3-element vectors (LxWxH)
        let line = line_result?;
        let trimmed = line.trim();
        let parts: Vec<&str> = trimmed.split("x").collect();

        let l: i32 = parts[0].parse().expect("Not a valid number");
        let w: i32 = parts[1].parse().expect("Not a valid number");
        let h: i32 = parts[2].parse().expect("Not a valid number");

        let side1 = l*w*2;
        let side2 = w*h*2;
        let side3 = h*l*2;

        let area1 = l*w;
        let area2 = l*h;
        let area3 = w*h;

        let smallest_side = cmp::min(area1, cmp::min(area2, area3));
        total_surface_area += side1+side2+side3+smallest_side;
    }
    println!("Part 1 Solution: {}", total_surface_area);

    // Solution 2
    println!("Part 2 Solution: {}",0);
    // "Return 0"
    Ok(())
}