use std::fs;

struct Range {
    low: u32,
    high: u32,
}

fn main() {
    println!("{}", part1());
    println!("{}", part2());
}

fn part1() -> u32 {
    let content = fs::read_to_string("input.txt").unwrap();

    content.lines().fold(0, |total, s| {
        let mut split = s.split(",");
        let range1 = Range::from(split.nth(0).unwrap());
        let range2 = Range::from(split.nth(0).unwrap());

        total
            + match range1.check_inside(&range2) {
                true => 1,
                false => 0,
            }
    })
}

fn part2() -> u32 {
    let content = fs::read_to_string("input.txt").unwrap();

    content.lines().fold(0, |total, s| {
        let mut split = s.split(",");

        let range1 = Range::from(split.nth(0).unwrap());
        let range2 = Range::from(split.nth(0).unwrap());

        total
            + match range1.check_overlap(&range2) {
                true => 1,
                false => 0,
            }
    })
}

impl Range {
    fn check_inside(&self, other: &Range) -> bool {
        if self.low <= other.low && self.high >= other.high {
            true
        } else if other.low <= self.low && other.high >= self.high {
            true
        } else {
            false
        }
    }

    fn check_overlap(&self, other: &Range) -> bool {
        let v = (self.low..=self.high).collect::<Vec<_>>();

        (other.low..=other.high).filter(|n| v.contains(n)).count() != 0
    }
}

impl From<&str> for Range {
    fn from(s: &str) -> Self {
        let mut split = s.split("-");

        Range {
            low: split.nth(0).unwrap().parse().unwrap(),
            high: split.nth(0).unwrap().parse().unwrap(),
        }
    }
}
