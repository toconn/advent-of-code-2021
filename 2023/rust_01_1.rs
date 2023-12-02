mod rust_advent;
use rust_advent::*;
mod shared;
use shared::*;

const DAY: usize = 1;
const PART: usize = 1;

// Solution ───────────────────────────────────────────────────────────────── //

fn solve(lines: Vec<String>) -> isize {
	lines.iter().map(|line| solve_line(line)).sum()
}

fn solve_line(line: &str) -> isize {

	let numbers: Vec<isize> = line
		.chars().map(|char| char.to_digit(10))
		.filter(|value| value.is_some())
		.map(|value| value.unwrap() as isize).collect();

	println!("{:?}", &numbers);

	let Some(first) = numbers.first() else {
		panic!("No first number");
	};

	let Some(last) = numbers.last() else {
		panic!("No last number");
	};

	first * 10 + last
}

// Main ───────────────────────────────────────────────────────────────────── //

fn main() {
	nl();
	// run_test(DAY, PART, solve);
	run_actual(DAY, PART, solve);
}