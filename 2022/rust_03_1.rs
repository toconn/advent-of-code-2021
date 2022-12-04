mod rust_shared;
use rust_shared::*;

const DAY: usize = 3;
const PART: usize = 1;

// Solution ───────────────────────────────────────────────────────────────── //

fn solve(lines: Vec<String>) -> isize {
	lines.iter().map(|line| score(get_duplicate(line))).sum()
}

fn contains(value: &str, character: char) -> bool {
    value.chars().any(|item| item == character)
}

fn get_duplicate(letters: &str) -> char {

	let split = letters.chars().count() / 2;
	let first = letters[..split].to_string();
	let second = letters[split..].to_string();
	
	for letter in first.chars() {
		if contains(&second, letter) {
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