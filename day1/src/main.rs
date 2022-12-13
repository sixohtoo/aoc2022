use std::cmp::max;
use std::fs;

fn main() {
    println!("{}", part1());
    println!("{}", part2());
}

fn part1() -> i32 {
    let contents = fs::read_to_string("input.txt").unwrap();

    let largest = contents
        .lines()
        .fold((0, 0), |current: (i32, i32), new| match new {
            "" => (max(current.0, current.1), 0),
            _ => (current.0, current.1 + new.trim().parse::<i32>().unwrap()),
        });

    largest.0
}

fn part2() -> i32 {
    let contents = fs::read_to_string("input.txt").unwrap();

    let largest = contents.lines().fold(
        (Vec::<i32>::new(), 0),
        |mut current: (Vec<i32>, i32), new| match new {
            "" => {
                current.0.push(current.1);
                (current.0, 0)
            }
            _ => (current.0, current.1 + new.trim().parse::<i32>().unwrap()),
        },
    );

    let mut calories = largest.0;
    calories.sort_by(|a, b| b.cmp(a));

    calories[0] + calories[1] + calories[2]
}
