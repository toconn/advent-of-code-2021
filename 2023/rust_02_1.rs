mod rust_advent;
use rust_advent::*;
mod shared;
use shared::*;

const DAY: usize = %day%;
const PART: usize = %part%;


// Types ──────────────────────────────────────────────────────────────────── //

struct Piece {
	color: String,
	count: usize
}

impl Piece {
	fn new(color: String, count: usize) -> Piece {
		Piece { color: color, count: count }
	}
}

struct Pieces {
	red: usize,
	green: usize,
	blue: usize;
}

impl Pieces {

	fn default() -> Pieces {
		Pieces { red: 0, green: 0, blue: 0 }
	}

	fn new(red: usize, green: usize, blue: usize) -> Pieces {
		Pieces { red: red, green: green, blue: blue }
	}
}

// Solution ───────────────────────────────────────────────────────────────── //

fn solve(lines: Vec<String>) -> isize {
	lines.iter().map(|line| solve_line(line)).sum()
}

fn solve_line(line: &str) -> isize {
	0
}

fn game_id(line: &str) -> usize {
	line.split(" ").last().unwrap().split(":").next().unwrap().parse::<usize>().unwrap()
}

fn to_games_and_results(lines: Vec<String>) -> Vec<Pieces> {
	// Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
	let games = line.split(":").last.unwrap().split(";").collect::<Vec<&str>>();

}

fn to_pieces(pieces: &str) -> Pieces {
	// 3 blue, 4 red
	let parts = pieces.split(";").collect::<Vec<&str>>();
	for part in parts {
		let piece = to_piece(part);
	}
}

fn to_piece(piece: &str) -> Piece {
	// 3 blue
	let parts = piece.trim().split(" ").collect::<Vec<&str>>();
	let count = parts[0].parse::<usize>().unwrap();
	let color = parts[1];
	Piece::new(color, count)
}

// Main ───────────────────────────────────────────────────────────────────── //

fn main() {

	nl();
	match has_argument("test") or has_argument("t") {
		true => run_test(DAY, PART, solve);
		false => run_actual(DAY, PART, solve);
	}
}