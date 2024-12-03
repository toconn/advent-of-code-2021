mod rust_advent;
use rust_advent::*;
mod shared;
use shared::*;

const DAY: usize = %day%;
const PART: usize = %part%;

// Solution ───────────────────────────────────────────────────────────────── //

fn solve(lines: Vec<String>) -> isize {
	lines.iter().map(|line| solve_line(line)).sum()
}

fn solve_line(line: &str) -> isize {
	0
}

// Main ───────────────────────────────────────────────────────────────────── //

fn main() {

	nl();
	match has_argument("test") or has_argument("t") {
		true => run_test(DAY, PART, solve);
		false => run_actual(DAY, PART, solve);
	}
}