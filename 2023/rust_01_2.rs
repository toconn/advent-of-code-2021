mod rust_advent;
use rust_advent::*;
mod shared;
use shared::*;
const DAY: usize = 1;
const PART: usize = 2;

const DIGITS: [&str; 9] = [
	"one", "two", "three", "four", "five", "six", "seven", "eight", "nine"
];

// Solution ───────────────────────────────────────────────────────────────── //

fn solve(lines: Vec<String>) -> isize {
	lines.iter().map(|line| solve_line(line)).sum()
}

fn solve_line(line: &str) -> isize {

	// println!("{}", line);

	let first = get_first_digit(line);
	let last = get_last_digit(line);

	// println!("[{}, {}]", first, last);

	first * 10 + last
}

fn get_first_digit(line: &str) -> isize {

	let chars = line.chars().collect::<Vec<char>>();

	for index in 0..=(chars.len() - 1) {

		if chars[index].is_digit(10) {
			return chars[index].to_digit(10).unwrap() as isize;
		}

		let remainder = chars[index..].iter().collect::<String>();

		if let Some(digit) = to_start_digit(&remainder) {
			return digit;
		}
	}

	panic!("No first digit");
}

fn get_last_digit(line: &str) -> isize {

	let chars = line.chars().collect::<Vec<char>>();

	for index in (0..=(chars.len() - 1)).rev() {

		if chars[index].is_digit(10) {
			return chars[index].to_digit(10).unwrap() as isize;
		}

		let remainder = chars[..index + 1].iter().collect::<String>();
		if let Some(digit) = to_end_digit(&remainder) {
			return digit;
		}
	}

	panic!("No last digit");
}

fn to_end_digit(line: &str) -> Option<isize> {

	for (index, digit) in DIGITS.iter().enumerate() {
		if line.ends_with(digit) {
			return Some((index + 1) as isize)
		}
	}
	None
}

fn to_start_digit(line: &str) -> Option<isize> {

	for (index, digit) in DIGITS.iter().enumerate() {
		if line.starts_with(digit) {
			return Some((index + 1) as isize)
		}
	}

	None
}

// Main ───────────────────────────────────────────────────────────────────── //

fn main() {
	nl();
	// run_test(DAY, PART, solve);
	run_actual(DAY, PART, solve);
}