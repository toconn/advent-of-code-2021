#![allow(unused)]

use std::any::type_name;
use std::env;
use std::error::Error;
use std::fmt::Display;
use std::fs::metadata;
use std::fs::remove_file;
use std::path::MAIN_SEPARATOR;
use std::path::Path;
use std::time::SystemTime;
use std::thread::sleep;
use std::time::Duration;
use std::time::Instant;

const HEADING_WIDTH: usize = 60;
const TITLE_WIDTH: usize = 80;
const COLUMN_1_WIDTH: usize = 20;

// Constants - Colors ─────────────────────────────────── //

pub static DEFAULT_COLOR: &str = "\x1b[0m";
pub static DEFAULT_BACKGROUND: &str = "\x1b[49m";
pub static RESET_COLOR: &str = "\x1b[0m";
pub static RESET: &str = "\x1b[0m";

// Foreground:

pub static BLACK: &str = "\x1b[30m";
pub static DARK_GRAY: &str = "\x1b[90m";
pub static LIGHT_GRAY: &str = "\x1b[37m";
pub static WHITE: &str = "\x1b[97m";
pub static BLUE: &str = "\x1b[34m";
pub static CYAN: &str = "\x1b[36m";
pub static GREEN: &str = "\x1b[32m";
pub static PURPLE: &str = "\x1b[35m";
pub static MAGENTA: &str = "\x1b[35m";
pub static RED: &str = "\x1b[31m";
pub static YELLOW: &str = "\x1b[33m";
pub static LIGHT_BLUE: &str = "\x1b[94m";
pub static LIGHT_CYAN: &str = "\x1b[96m";
pub static LIGHT_GREEN: &str = "\x1b[92m";
pub static LIGHT_PURPLE: &str = "\x1b[95m";
pub static LIGHT_MAGENTA: &str = "\x1b[95m";
pub static LIGHT_RED: &str = "\x1b[91m";
pub static LIGHT_YELLOW: &str = "\x1b[93m";

// Background:

pub static ON_BLACK: &str = "\x1b[40m";
pub static ON_DARK_GRAY: &str = "\x1b[100m";
pub static ON_LIGHT_GRAY: &str = "\x1b[47m";
pub static ON_WHITE: &str = "\x1b[107m";
pub static ON_BLUE: &str = "\x1b[44m";
pub static ON_CYAN: &str = "\x1b[46m";
pub static ON_GREEN: &str = "\x1b[42m";
pub static ON_PURPLE: &str = "\x1b[45m";
pub static ON_MAGENTA: &str = "\x1b[45m";
pub static ON_RED: &str = "\x1b[41m";
pub static ON_YELLOW: &str = "\x1b[43m";
pub static ON_LIGHT_BLUE: &str = "\x1b[104m";
pub static ON_LIGHT_CYAN: &str = "\x1b[106m";
pub static ON_LIGHT_GREEN: &str = "\x1b[102m";
pub static ON_LIGHT_MAGENTA: &str = "\x1b[105m";
pub static ON_LIGHT_PURPLE: &str = "\x1b[105m";
pub static ON_LIGHT_RED: &str = "\x1b[101m";
pub static ON_LIGHT_YELLOW: &str = "\x1b[103m";

// Styles:

pub static BOLD: &str = "\x1b[1m";
pub static BLINK: &str = "\x1b[5m";
pub static DIMMED: &str = "\x1b[2m";
pub static ITALIC: &str = "\x1b[3m";
pub static REVERSED: &str = "\x1b[7m";
pub static STRIKETHROUGH: &str = "\x1b[9m";
pub static UNDERLINE: &str = "\x1b[4m";

pub static ERROR: &str = "\x1b[1m\x1b[91m"; // Bold Light Red
pub static INFO: &str = "\x1b[92m"; // Light Green
pub static WARNING: &str = "\x1b[1m\x1b[93m"; // Bold Light Yellow

pub static COMMAND: &str = "\x1b[93m"; // Light Yellow
pub static VAR: &str = "\x1b[3m\x1b[95m"; // Italic Light Magenta
pub static VARIABLE: &str = "\x1b[3m\x1b[95m"; // Italic Light Magenta


// File Constants ─────────────────────────────────────── //

#[cfg(target_os = "windows")]
pub const PATH_SEPARATOR: &str = ";";

#[cfg(not(target_os = "windows"))]
pub const PATH_SEPARATOR: &str = ":";


// Types ──────────────────────────────────────────────── //

pub struct First {
    first: bool,
}

impl First {
    pub fn new() -> Self {
        First { first: true }
    }
    pub fn is_first(&mut self) -> bool {
        if !self.first {
            return false;
        }

        self.first = false;
        return true;
    }

    pub fn not_first(&mut self) -> bool {
        return !self.is_first();
    }
}

pub struct Timer {
    start: Instant,
    stop: Option<Instant>,
}

impl Timer {
    pub fn new() -> Self {
        Timer {
            start: Instant::now(),
            stop: None,
        }
    }

    pub fn start(&mut self) {
        self.start = Instant::now();
        self.stop = None;
    }

    pub fn stop(&mut self) -> Duration {
        self.stop = Some(Instant::now());
        return self.duration();
    }

    pub fn duration(&self) -> Duration {
        match self.stop {
            Some(stop) => stop.duration_since(self.start),
            None => self.start.elapsed(),
        }
    }

    pub fn duration_formatted(&self) -> String {
        let seconds = self.seconds();
        let seconds = seconds.floor() as u128;
        let milliseconds = self.milliseconds() - seconds * 1000;

        if seconds > 0 {
            f!("{} s  {:03} ms", seconds, milliseconds)
        } else {
            f!("{} ms", milliseconds)
        }
    }

    pub fn microseconds(&self) -> u128 {
        self.duration().as_micros()
    }

    pub fn milliseconds(&self) -> u128 {
        self.duration().as_millis()
    }

    pub fn seconds(&self) -> f64 {
        self.duration().as_secs_f64()
    }
}

pub type E = Box<dyn Error>;
pub type ResultsInOk = Result<(), Box<dyn Error>>;
pub type ResultsIn<T> = Result<T, Box<dyn Error>>;
pub type RInOk = Result<(), Box<dyn Error>>;
pub type RIn<T> = Result<T, Box<dyn Error>>;

pub struct Wrap<T>(pub T);

pub use std::format as f;
pub use std::println as p;
pub use std::result::Result as R;

// Arguments ──────────────────────────────────────────── //

pub fn argument(index: usize) -> Option<String> {
    env::args().nth(index + 1)
}

pub fn argument_count() -> usize {
    env::args().count() - 1
}

pub fn argument_is(index: usize, text: &str) -> bool {
    match argument(index) {
        Some(arg) => arg.to_lowercase() == text.to_lowercase(),
        None => false,
    }
}

pub fn arguments() -> Vec<String> {
    env::args().skip(1).collect()
}

pub fn has_arguments() -> bool {
    env::args().count() > 1
}

pub fn no_arguments() -> bool {
    !has_arguments()
}

// File Utils ─────────────────────────────────────────── //

pub fn delete_file(path: &str) {
    if file_exists(&path) {
        remove_file(&path);
    }
}

pub fn file_exists(path: &str) -> bool {
    Path::new(path).exists()
}

/// Returns the modified time of a file.
/// If not present or error, returns None.
pub fn file_modified(file_name: &str) -> Option<SystemTime> {
    let metadata = metadata(file_name);
    if metadata.is_err() {
        return None;
    }

    match metadata.unwrap().modified() {
        Ok(time) => Some(time),
        Err(_) => None,
    }
}

pub fn file_not_found(path: &str) -> bool {
    !file_exists(path)
}

pub fn join(directory: &str, file: &str) -> String {
    format!("{}{}{}", directory, MAIN_SEPARATOR, file)
}


// File Name Utils ────────────────────────────────────── //

/// Returns the directory path of a file.
/// Example: "/user/your_name_here/file.txt" returns "/user/your_name_here"
pub fn file_directory(path: &str) -> String {

    if path.ends_with(MAIN_SEPARATOR) {
        return remove_suffix(path, &MAIN_SEPARATOR.to_string());
    }

    match Path::new(path).extension() {
        Some(directory) => {
            match directory.to_str() {
                Some(directory) => directory.to_string(),
                None => "".to_string(),
            }
        },
        None => "".to_string(),
    }
}

/// Returns the file name with the extension but without the path.
/// Example: "/path/file.txt" returns "file.txt"
pub fn file_name(path: &str) -> Option<String> {
    Some(Path::new(path).file_name()?.to_str()?.to_string())
}

/// Returns the file name without the extension or path.
/// Example: "/path/file.txt" returns "file"
pub fn file_stem(path: &str) -> Option<String> {
    Some(Path::new(path).file_stem()?.to_str()?.to_string())
}

// String Utils ───────────────────────────────────────── //

pub fn is_blank(text: &str) -> bool {
    return text.trim().is_empty();
}

pub fn is_comment(text: &str) -> bool {
    let trimmed = text.trim();
    return trimmed.starts_with("#") || trimmed.starts_with("//");
}

pub fn is_empty(text: &str) -> bool {
    return text.is_empty();
}

pub fn not_blank(text: &str) -> bool {
    return !is_blank(text);
}

pub fn not_comment(text: &str) -> bool {
    return !is_comment(text);
}

pub fn not_empty(text: &str) -> bool {
    return !is_empty(text);
}

pub fn pad(text: &str, length: usize) -> String {
    if text.len() >= length {
        return format!("{}", text);
    }
    return format!("{}{}", text, " ".repeat(length - text.len()));
}

pub fn pad_column_1(text: &str) -> String {
    pad(&text, COLUMN_1_WIDTH)
}

fn remove_first(text: &str) -> &str {
    text.char_indices().next().map(|(length, _)| &text[length..]).unwrap_or("")
}

pub fn remove_prefix(text: &str, prefix: &str) -> String {
    if let Some(text) = text.strip_prefix(prefix) {
        return text.to_string();
    }
    return text.to_string();
}

pub fn remove_suffix(text: &str, prefix: &str) -> String {
    if let Some(text) = text.strip_suffix(prefix) {
        return text.to_string();
    }
    return text.to_string();
}

/// Converts an array of &str into a vec of Strings.
pub fn to_vec(items: &[&str]) -> Vec<String> {
    items.iter().map(|item| item.to_string()).collect()
}

pub fn type_of<T>(_: T) -> &'static str {
    type_name::<T>()
}

// Print Functions ────────────────────────────────────── //

pub fn bar() {
    color(LIGHT_GREEN, &"─".repeat(HEADING_WIDTH));
}

pub fn color(color: &str, value: &str) {
    print_color(color, value);
}

pub fn error(label: &str, error: &Box<dyn Error>) {
    print_error(label, error);
}

pub fn heading(value: &str) {
    heading_bar(value, true);
    nl();
}

pub fn heading_bar(value: &str, fill: bool) {
    let fill_char = if fill { "─" } else { " " };
    let trailing_stars = fill_char.repeat(HEADING_WIDTH - 6 - value.chars().count());
    println!(
        "{}──  {}  {}{}",
        LIGHT_GREEN, value, trailing_stars, RESET_COLOR
    );
}

pub fn info(text: &str) {
    color(INFO, text);
}

pub fn nl() {
    println!("");
}

pub fn nl2() {
    nl();
    nl();
}

pub fn print(value: &str) {
    println!("{}", value);
}

pub fn print_array<T: Display>(label: &str, items: &[T]) {
    let mut first = First::new();

    if items.len() == 0 {
        println!("{}  [ N/A ]", pad_column_1(&label));
        return;
    }

    for item in items {
        if first.is_first() {
            println!("{}  {}", pad_column_1(&label), &item.to_string());
        } else {
            println!("{}  {}", pad_column_1(&""), &item.to_string());
        }
    }
}

pub fn print_color(color: &str, text: &str) {
    println!("{}{}{}", color, text, RESET_COLOR);
}

pub fn print_double(value: &str) {
    println!("{}", value);
    nl();
}

pub fn print_error(label: &str, error: &Box<dyn Error>) {
    println!("{}{} : {}{}", &LIGHT_RED, label, error, &RESET_COLOR);
}

pub fn print_vec<T: Display>(label: &str, items: &Vec<T>) {
    let mut first = First::new();

    if items.len() == 0 {
        println!("{}  [ N/A ]", pad_column_1(&label));
        return;
    }

    for item in items {
        if first.is_first() {
            println!("{}  {}", pad_column_1(&label), &item.to_string());
        } else {
            println!("{}  {}", pad_column_1(&""), &item.to_string());
        }
    }
}

pub fn short_heading(value: &str) {
    println!("{}──  {}  ──{}", LIGHT_GREEN, value, RESET_COLOR);
    nl();
}

pub fn title(value: &str) {
    println!("{}┌{}┐", GREEN, "─".repeat(TITLE_WIDTH - 2));
    title_bar(&value, false);
    println!("└{}┘{}", "─".repeat(TITLE_WIDTH - 2), RESET_COLOR);
    nl();
}

pub fn title_bar(value: &str, fill: bool) {
    let fill_char = if fill { "─" } else { " " };
    let trailing_stars = fill_char.repeat(TITLE_WIDTH - 5 - value.chars().count());
    println!("│ {} {} │", value, trailing_stars);
}

pub fn warning(text: &str) {
    color(WARNING, text);
}


// System Utils ───────────────────────────────────────── //

pub fn sleep_ms(milliseconds: u64) {
    sleep(Duration::from_millis(milliseconds));
}