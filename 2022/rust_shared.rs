#![allow(unused)]

use std::any::type_name;
use std::fs::read_to_string;

// AOC ─────────────────────────────────────────────────── //

const DATA_DIR: &str = "data/";
const DATA_FILE: &str = "-data.txt";
const TEST_FILE: &str = "-test.txt";
const TEST_ANSWERS_FILE: &str = "-test-answers.txt";

fn path(day: usize, postfix: &str) -> String {
    format!("{}{:02}{}", DATA_DIR, day, postfix)
}

pub fn read_data(day: usize) -> Vec<String> {
    read_trimmed_lines(&path(day, DATA_FILE))
}

pub fn read_test(day: usize) -> Vec<String> {
    read_trimmed_lines(&path(day, TEST_FILE))
}

pub fn read_test_answer(day: usize, index: usize) -> isize {
    let lines = read_trimmed_lines(&path(day, TEST_ANSWERS_FILE));
    lines[index - 1].parse().unwrap()
}

// AOC - Main ─────────────────────────────────────────── //

pub fn run_test(day: usize, part: usize, solve: fn(Vec<String>) -> isize) {
    nl();
    solve_test(day, part, solve);
    nl();
}

pub fn run_test_and_actual(day: usize, part: usize, solve: fn(Vec<String>) -> isize) {
    nl();
    solve_test(day, part, solve);
    solve_actual(day, solve);
    nl();
}

fn solve_actual(day: usize, solve: fn(Vec<String>) -> isize) {
    let answer = solve(read_data(day));
    println!("Answer: {:<6}", answer)
}

fn solve_test(day: usize, part: usize, solve: fn(Vec<String>) -> isize) {
    let expected = read_test_answer(day, part);
    let actual = solve(read_test(day));

    if actual == expected {
        println!("Test:   {:<6} 👍", actual);
    }
    else {
        println!("Test:   {:<6} (≠ {}) ❌", actual, expected);
    }
}

// Types ──────────────────────────────────────────────── //

pub struct Wrap<T>(pub T);

pub use std::format as f;
pub use std::println as p;
pub use std::result::Result as R;

// File ───────────────────────────────────────────────── //

pub fn read(path: &str) -> String {
    read_to_string(path).unwrap()
}

pub fn read_lines(path: &str) -> Vec<String> {
    read(path).lines().map(|item|item.to_string()).collect()
}

pub fn read_trimmed_lines(path: &str) -> Vec<String> {
    read(path).trim().lines().map(|item|item.to_string()).collect()
}

// Strings ────────────────────────────────────────────── //

pub fn pad(text: &str, length: usize) -> String {
    if text.len() >= length {
        return format!("{}", text);
    }
    return format!("{}{}", text, " ".repeat(length - text.len()));
}

// Print ──────────────────────────────────────────────── //

const COLUMN_1_WIDTH: usize = 30;

pub fn pad_column_1(text: &str) -> String {
    pad(&text, COLUMN_1_WIDTH)
}

pub fn type_of<T>(_: T) -> &'static str {
    type_name::<T>()
}

pub fn nl() {
    println!("");
}
