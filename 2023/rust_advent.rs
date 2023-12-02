#![allow(unused)]

use std::any::type_name;
use std::fs::read_to_string;
use crate::shared::nl;

// AOC ─────────────────────────────────────────────────── //

const DATA_DIR: &str = "data/";
const DATA_FILE: &str = "d";
const TEST_FILE: &str = "t";
const TEST_ANSWERS_FILE: &str = "a";

pub fn read_data(day: usize, part: usize) -> Vec<String> {
    read_trimmed_lines(&to_path(day, part, DATA_FILE))
}

pub fn read_test(day: usize, part: usize) -> Vec<String> {
    read_trimmed_lines(&to_path(day, part, TEST_FILE))
}

pub fn read_test_answer(day: usize, part: usize) -> isize {
    let lines = read_trimmed_lines(&to_path(day, part, TEST_ANSWERS_FILE));
    lines[0].parse().unwrap()
}

pub fn to_path(day: usize, part: usize, postfix: &str) -> String {
    f!("{}{:>02}-{}-{}.txt", DATA_DIR, day, part, postfix)
}

// AOC - Main ─────────────────────────────────────────── //

pub fn run_actual(day: usize, part: usize, solve: fn(Vec<String>) -> isize) {
    solve_actual(day, part, solve);
    nl();
}

pub fn run_test(day: usize, part: usize, solve: fn(Vec<String>) -> isize) {
    nl();
    solve_test(day, part, solve);
    nl();
}

pub fn run_test_and_actual(day: usize, part: usize, solve: fn(Vec<String>) -> isize) {
    run_test(day, part, solve);
    run_actual(day, part, solve);
}

fn solve_actual(day: usize, part: usize, solve: fn(Vec<String>) -> isize) {
    let answer = solve(read_data(day, part));
    nl();
    println!("Answer: {:<6}", answer)
}

fn solve_test(day: usize, part: usize, solve: fn(Vec<String>) -> isize) {
    let expected = read_test_answer(day, part);
    let actual = solve(read_test(day, part));

    nl();
    match actual == expected {
        true => println!("Test:   {:<6} 👍", actual),
        false => println!("Test:   {:<6} (≠ {}) ❌", actual, expected),
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
