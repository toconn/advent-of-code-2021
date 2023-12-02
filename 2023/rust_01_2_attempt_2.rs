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

	println!("{}", line);
	let line = to_digits(line);
	println!("{}", line);

	let numbers: Vec<isize> = line
		.chars().map(|char| char.to_digit(10))
		.filter(|value| value.is_some())
		.map(|value| value.unwrap() as isize).collect();


	let Some(first) = numbers.first() else {
		panic!("No first number");
	};

	let Some(last) = numbers.last() else {
		panic!("No last number");
	};

	println!("{:?}", &numbers);
	println!("[{}, {}]", first, last);
	nl();

	first * 10 + last
}

fn to_digits(line: &str) -> String {

	let mut min_index = 0;
	let mut min = line.len();
	let mut max_index = 0;
	let mut max = 0;

	for (index, digit) in DIGITS.iter().enumerate() {

		if let Some(position) = line.find(digit) {
			if position < min {
				min = position;
				min_index = index;
			}
		}

		if let Some(position) = line.rfind(digit) {
			if position > max {
				max = position;
				max_index = index;
			}
		}


	}
	
	line.replace(DIGITS[min_index], &f!("{}", min_index + 1)).replace(DIGITS[max_index], &f!("{}", max_index + 1))
}

// Main ───────────────────────────────────────────────────────────────────── //

fn main() {
	nl();
	// run_test(DAY, PART, solve);
	run_actual(DAY, PART, solve);
}