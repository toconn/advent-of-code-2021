mod rust_shared;
use rust_shared::*;

const DAY: usize = 3;
const PART: usize = 2;

// Solution ───────────────────────────────────────────────────────────────── //

fn solve(lines: Vec<String>) -> isize {

	let mut answer = 0;
	for i in (0..lines.len()).step_by(3) {
		answer += score(find_duplicate(&lines[i], &lines[i+1], &lines[i+2]));
	}
	answer
}

fn contains(value: &str, character: char) -> bool {
    value.chars().any(|item| item == character)
}

fn find_duplicate(first: &str, second: &str, third: &str) -> char {
	
	for letter in first.chars() {
		if contains(&second, letter) && contains(&third, letter) {
			return letter;
		}
	}
	panic!("Duplicate not found!");
}

fn score(letter: char) -> isize {
	(letter as isize) - (if letter > 'Z' {96} else {38})
}

// Main ───────────────────────────────────────────────────────────────────── //

fn main() {
	// run_test(DAY, PART, solve);
	run_test_and_actual(DAY, PART, solve);
}