use std::cmp::min;
use std::fs;

fn main() {
    println!("{}", part1());
    println!("{}", part2());
}

fn part1() -> String {
    let content = fs::read_to_string("input.txt").unwrap();
    let lines = content.lines();

    let num_columns: usize = (content.lines().nth(0).unwrap().len() + 1) / 4;

    let mut columns = Vec::<Vec<char>>::new();

    for i in 0..num_columns {
        columns.insert(i, Vec::<char>::new());
    }

    let mut parsing = true;
    lines.fold(true, |parsing, line| {
        if line == "" {
            false
        } else {
            match parsing {
                true => {
                    line.chars().enumerate().for_each(|(i, c)| {
                        if c.is_ascii_uppercase() {
                            let column = columns.get_mut(i / 4).unwrap();
                            column.push(c);
                        }
                    });
                    true
                }
                false => {
                    let mut split = line.split(" ");
                    let num: usize = split.nth(1).unwrap().parse().unwrap();
                    let from: usize = split.nth(1).unwrap().parse::<usize>().unwrap() - 1;
                    let to: usize = split.nth(1).unwrap().parse::<usize>().unwrap() - 1;
                    let from_len = columns.get(from).unwrap().len();

                    for _ in 0..=(min(num, from_len) - 1) {
                        let item = {
                            let from_column = columns.get_mut(from).unwrap();
                            from_column.remove(0)
                        };

                        let to_column = columns.get_mut(to).unwrap();
                        to_column.insert(0, item)
                    }
                    false
                }
            }
        }
    });

    columns
        .into_iter()
        .map(|v| v.into_iter().nth(0).unwrap_or_default())
        .collect::<String>()
}

fn part2() -> String {
    let content = fs::read_to_string("input.txt").unwrap();
    let lines = content.lines();

    let num_columns: usize = (content.lines().nth(0).unwrap().len() + 1) / 4;

    let mut columns = Vec::<Vec<char>>::new();

    for i in 0..num_columns {
        columns.insert(i, Vec::<char>::new());
    }

    let mut parsing = true;
    lines.fold(true, |parsing, line| {
        if line == "" {
            false
        } else {
            match parsing {
                true => {
                    line.chars().enumerate().for_each(|(i, c)| {
                        if c.is_ascii_uppercase() {
                            let column = columns.get_mut(i / 4).unwrap();
                            column.push(c);
                        }
                    });
                    true
                }
                false => {
                    let mut split = line.split(" ");
                    let num: usize = split.nth(1).unwrap().parse().unwrap();
                    let from: usize = split.nth(1).unwrap().parse::<usize>().unwrap() - 1;
                    let to: usize = split.nth(1).unwrap().parse::<usize>().unwrap() - 1;
                    let from_len = columns.get(from).unwrap().len();

                    let mut removed: Vec<char> = Vec::new();
                    for _ in 0..=(min(num, from_len) - 1) {
                        removed.insert(0, {
                            let from_column = columns.get_mut(from).unwrap();
                            from_column.remove(0)
                        });
                    }

                    let to_column = columns.get_mut(to).unwrap();
                    removed.into_iter().for_each(|c| {
                        to_column.insert(0, c);
                    });

                    // to_column.splice(0..=0, removed.into_iter());
                    false
                }
            }
        }
    });

    columns
        .into_iter()
        .map(|v| v.into_iter().nth(0).unwrap_or_default())
        .collect::<String>()
}
