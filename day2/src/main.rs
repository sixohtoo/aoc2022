use std::{collections::HashMap, fmt::Debug, fs};

#[derive(Clone, Copy)]
enum Outcome {
    Win,
    Tie,
    Lose,
}

#[derive(Clone, Copy, PartialEq, Hash, Eq)]
enum Gesture {
    Rock,
    Paper,
    Scissors,
}

fn main() {
    println!("{}", part1());
    println!("{}", part2());
}

fn part1() -> i32 {
    let content = fs::read_to_string("input.txt").unwrap();

    content.lines().fold(0, |curr_total, line| {
        let mut split = line.split(" ");

        let first = Gesture::from(split.nth(0).unwrap());
        let second = Gesture::from(split.nth(0).unwrap());

        let outcome = Outcome::from((first, second));

        curr_total + i32::from(second) + i32::from(outcome)
    })
}

fn part2() -> i32 {
    let content = fs::read_to_string("input.txt").unwrap();
    content.lines().fold(0, |curr_total, line| {
        let mut split = line.split(" ");
        let gesture = Gesture::from(split.nth(0).unwrap());
        let outcome = Outcome::from(split.nth(0).unwrap());

        let second = Gesture::from((gesture, outcome.clone()));

        curr_total + i32::from(second) + i32::from(outcome)
    })
}

impl From<(Gesture, Gesture)> for Outcome {
    fn from((first, second): (Gesture, Gesture)) -> Self {
        let pairings = HashMap::from([
            (Gesture::Rock, Gesture::Paper),
            (Gesture::Paper, Gesture::Scissors),
            (Gesture::Scissors, Gesture::Rock),
        ]);

        if first == second {
            Outcome::Tie
        } else if pairings.get(&first).unwrap() == &second {
            Outcome::Win
        } else {
            Outcome::Lose
        }
    }
}

impl From<&str> for Outcome {
    fn from(s: &str) -> Self {
        match s {
            "X" => Outcome::Lose,
            "Y" => Outcome::Tie,
            "Z" => Outcome::Win,
            _ => panic!("tf"),
        }
    }
}

impl From<Outcome> for i32 {
    fn from(o: Outcome) -> Self {
        match o {
            Outcome::Win => 6,
            Outcome::Tie => 3,
            Outcome::Lose => 0,
        }
    }
}

impl Debug for Outcome {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        let s = match self {
            Outcome::Win => "Win",
            Outcome::Tie => "Tie",
            Outcome::Lose => "Lose",
        };
        write!(f, "{}", s)
    }
}

impl From<&str> for Gesture {
    fn from(input: &str) -> Self {
        match input {
            "A" | "X" => Gesture::Rock,
            "B" | "Y" => Gesture::Paper,
            "C" | "Z" => Gesture::Scissors,
            _ => panic!("tf"),
        }
    }
}

impl From<Gesture> for i32 {
    fn from(g: Gesture) -> Self {
        match g {
            Gesture::Rock => 1,
            Gesture::Paper => 2,
            Gesture::Scissors => 3,
        }
    }
}

impl From<(Gesture, Outcome)> for Gesture {
    fn from((g, o): (Gesture, Outcome)) -> Self {
        let pairings_win = HashMap::from([
            (Gesture::Rock, Gesture::Paper),
            (Gesture::Paper, Gesture::Scissors),
            (Gesture::Scissors, Gesture::Rock),
        ]);

        let pairings_lose = HashMap::from([
            (Gesture::Paper, Gesture::Rock),
            (Gesture::Rock, Gesture::Scissors),
            (Gesture::Scissors, Gesture::Paper),
        ]);

        match o {
            Outcome::Win => *pairings_win.get(&g).unwrap(),
            Outcome::Tie => g,
            Outcome::Lose => *pairings_lose.get(&g).unwrap(),
        }
    }
}

impl Debug for Gesture {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        let s = match self {
            Gesture::Rock => "Rock",
            Gesture::Paper => "Paper",
            Gesture::Scissors => "Scissors",
        };
        write!(f, "{}", s)
    }
}
