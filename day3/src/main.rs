use itertools::izip;
use std::{collections::HashSet, fs};

fn main() {
    println!("{}", part1());
    println!("{}", part2());
}

fn part1() -> u16 {
    let content = fs::read_to_string("input.txt").unwrap();

    content.lines().fold(0, |total, line| {
        let len = line.len() / 2;

        let first: String = line.chars().take(len).collect();
        let second: String = line.chars().skip(len).take(len).collect();

        let letter = first
            .chars()
            .fold(first.chars().nth(0).unwrap(), |common, curr| {
                match second.contains(curr) {
                    true => curr,
                    false => common,
                }
            });

        total
            + match letter.is_ascii_uppercase() {
                true => letter as u16 - 'A' as u16 + 27,
                false => letter as u16 - 'a' as u16 + 1,
            }
    })
}

fn part2() -> u16 {
    let content = fs::read_to_string("input.txt").unwrap();

    let iter1 = content.lines().step_by(3);
    let iter2 = content.lines().skip(1).step_by(3);
    let iter3 = content.lines().skip(2).step_by(3);

    izip!(iter1, iter2, iter3).fold(0, |total, (first, second, third)| {
        let mut set1: HashSet<char> = HashSet::new();
        let mut set2: HashSet<char> = HashSet::new();
        let mut set3: HashSet<char> = HashSet::new();

        first.chars().for_each(|c| {
            set1.insert(c);
        });
        second.chars().for_each(|c| {
            set2.insert(c);
        });
        third.chars().for_each(|c| {
            set3.insert(c);
        });

        let inter = &(&set1 & &set2) & &set3;

        let letter = inter.iter().nth(0).unwrap();

        total
            + match letter.is_ascii_uppercase() {
                true => *letter as u16 - 'A' as u16 + 27,
                false => *letter as u16 - 'a' as u16 + 1,
            }
    })
}
