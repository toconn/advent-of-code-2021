package shared

import (
	"bufio"
	"fmt"
	"io"
	"os"
	"strconv"
	"strings"
)

const Column1Width = 30
const ColumnSeparator = ": "
const HeadingWidth = 60
const Indent = "    "
const Newline = "\n"
const ShortHeadingWidth = 40

// Colors ─────────────────────────────────────────────────────────────────── //

// Special Colors ─────────────────── //

const DEFAULT_COLOR = "\x1B[0m"
const DEFAULT_BACKGROUND = "\x1B[49m"
const RESET_COLOR = DEFAULT_COLOR + DEFAULT_BACKGROUND
const RESET = RESET_COLOR

// Foreground ─────────────────────── //

const BLACK = "\x1B[30m"
const DARK_GRAY = "\x1B[90m"
const LIGHT_GRAY = "\x1B[37m"
const WHITE = "\x1B[97m"
const BLUE = "\x1B[34m"
const CYAN = "\x1B[36m"
const GREEN = "\x1B[32m"
const PURPLE = "\x1B[35m"
const MAGENTA = "\x1B[35m"
const RED = "\x1B[31m"
const YELLOW = "\x1B[33m"
const LIGHT_BLUE = "\x1B[94m"
const LIGHT_CYAN = "\x1B[96m"
const LIGHT_GREEN = "\x1B[92m"
const LIGHT_PURPLE = "\x1B[95m"
const LIGHT_MAGENTA = "\x1B[95m"
const LIGHT_RED = "\x1B[91m"
const LIGHT_YELLOW = "\x1B[93m"

// Background ─────────────────────── //

const ON_BLACK = "\x1B[40m"
const ON_DARK_GRAY = "\x1B[100m"
const ON_LIGHT_GRAY = "\x1B[47m"
const ON_WHITE = "\x1B[107m"
const ON_BLUE = "\x1B[44m"
const ON_CYAN = "\x1B[46m"
const ON_GREEN = "\x1B[42m"
const ON_PURPLE = "\x1B[45m"
const ON_MAGENTA = "\x1B[45m"
const ON_RED = "\x1B[41m"
const ON_YELLOW = "\x1B[43m"
const ON_LIGHT_BLUE = "\x1B[104m"
const ON_LIGHT_CYAN = "\x1B[106m"
const ON_LIGHT_GREEN = "\x1B[102m"
const ON_LIGHT_PURPLE = "\x1B[105m"
const ON_LIGHT_MAGENTA = "\x1B[105m"
const ON_LIGHT_RED = "\x1B[101m"
const ON_LIGHT_YELLOW = "\x1B[103m"

// Styles ─────────────────────────── //

const BOLD = "\x1B[1m"
const BLINK = "\x1B[5m"
const DIMMED = "\x1B[2m"
const ITALIC = "\x1B[3m"
const REVERSED = "\x1B[7m"
const STRIKETHROUGH = "\x1B[9m"
const UNDERLINE = "\x1B[4m"

// User Defined ───────────────────── //

const ERROR = BOLD + LIGHT_RED
const INFO = LIGHT_GREEN
const WARNING = BOLD + LIGHT_YELLOW

const ANNOTATE = LIGHT_GRAY
const ANNOTE = ANNOTATE
const COMMAND = BOLD + YELLOW
const VAR = ITALIC + LIGHT_MAGENTA
const VARIABLE = VAR

// Files ──────────────────────────────────────────────────────────────────── //

// Returns true if the error indicates End of File (EOF).
func IsEndOfFile(err error) bool {
	return err != nil && err == io.EOF
}

// Reads a text file and returns all the lines as a slice
func ReadLines(path string) ([]string, error) {

	file, err := os.Open(path)

	if ReportOnError("Error opening file: "+path, err) {
		return nil, err
	}

	defer file.Close()

	var lines []string

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}

	return lines, nil
}

// Reads a text file and returns all the lines as a slice, but without comments or blank lines
func ReadLinesWithoutCommentsBlanks(path string) ([]string, error) {

	lines, err := ReadLines(path)
	if err != nil {
		return nil, err
	}

	return RemoveCommentsAndBlanks(lines), nil
}

// Strings ────────────────────────────────────────────────────────────────── //

func CharacterCount(text string) int {
	return len([]rune(text))
}

func IsBlank(text string) bool {
	return strings.TrimSpace(text) == ""
}

func IsComment(text string) bool {
	return strings.HasPrefix(text, "#") || strings.HasPrefix(text, "//")
}

func NotBlank(text string) bool {
	return !IsBlank(text)
}

func NotComment(text string) bool {
	return !IsComment(text)
}

func RemoveBlanks(lines []string) []string {

	var result []string

	for _, line := range lines {
		if NotBlank(line) {
			result = append(result, line)
		}
	}

	return result
}

func RemoveCommentsAndBlanks(lines []string) []string {

	var result []string

	for _, line := range lines {
		if NotBlank(line) && NotComment(line) {
			result = append(result, line)
		}
	}

	return result
}

func ToInt(text string) int {

	value, err := strconv.Atoi(text)

	ExitOnError("Couldn't convert to int: '" + text + "'", err)

	return value
}

func ToInts(items []string) []int {

	var ints []int

	for _, item  := range items {
		ints = append(ints, ToInt(item))
	}

	return ints
}

// System ─────────────────────────────────────────────────────────────────── //

func ExitOnError(message string, err error) {

	if err == nil {
		return
	}

	Error(message)
	print(err)
	os.Exit(2)
}

func ReportOnError(message string, err error) bool {

	if err == nil {
		return false
	}

	Error(message)
	print(err)
	return true
}

// UI ─────────────────────────────────────────────────────────────────────── //

func Error(message string) {
	fmt.Println(ERROR + message + RESET_COLOR)
}

func Heading(heading string) {

	prefix := "──  "
	formatted := prefix + heading + "  "

	count := CharacterCount(heading) + 6

	padded := formatted + strings.Repeat("─", HeadingWidth - count)

	fmt.Println(LIGHT_GREEN + padded + RESET_COLOR)
	fmt.Println()
}

func NL() {
	fmt.Println()
}

func ShortHeading(heading string) {

	prefix := "──  "
	formatted := prefix + heading + "  "

	count := CharacterCount(heading) + 6

	padded := formatted + strings.Repeat("─", ShortHeadingWidth - count)

	fmt.Println(LIGHT_GREEN + padded + RESET_COLOR)
	fmt.Println()
}

func Title(name string) {

	count := CharacterCount(name) + 4

	NL()
	// Line 1: Top border
	fmt.Print(GREEN)
	fmt.Println("┌─" + strings.Repeat("─", HeadingWidth - 4) + "─┐")

	// Line 2: Title with padding
	line := "│ " + name
	line = line + strings.Repeat(" ", HeadingWidth - count) + " │"
	fmt.Println(line)

	// Line 3: Bottom border
	fmt.Println("└─" + strings.Repeat("─", HeadingWidth - 4) + "─┘" + RESET_COLOR)

	NL()
}