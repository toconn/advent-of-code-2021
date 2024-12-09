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

const DefaultColor = "\x1B[0m"
const DefaultBackground = "\x1B[49m"
const ResetColor = DefaultColor + DefaultBackground
const Reset = ResetColor

// Foreground ─────────────────────── //

const Black = "\x1B[30m"
const DarkGray = "\x1B[90m"
const LightGray = "\x1B[37m"
const White = "\x1B[97m"
const Blue = "\x1B[34m"
const Cyan = "\x1B[36m"
const Green = "\x1B[32m"
const Purple = "\x1B[35m"
const Magenta = "\x1B[35m"
const Red = "\x1B[31m"
const Yellow = "\x1B[33m"
const LightBlue = "\x1B[94m"
const LightCyan = "\x1B[96m"
const LightGreen = "\x1B[92m"
const LightPurple = "\x1B[95m"
const LightMagenta = "\x1B[95m"
const LightRed = "\x1B[91m"
const LightYellow = "\x1B[93m"

// Background ─────────────────────── //

const OnBlack = "\x1B[40m"
const OnDarkGray = "\x1B[100m"
const OnLightGray = "\x1B[47m"
const OnWhite = "\x1B[107m"
const OnBlue = "\x1B[44m"
const OnCyan = "\x1B[46m"
const OnGreen = "\x1B[42m"
const OnPurple = "\x1B[45m"
const OnMagenta = "\x1B[45m"
const OnRed = "\x1B[41m"
const OnYellow = "\x1B[43m"
const OnLightBlue = "\x1B[104m"
const OnLightCyan = "\x1B[106m"
const OnLightGreen = "\x1B[102m"
const OnLightPurple = "\x1B[105m"
const OnLightMagenta = "\x1B[105m"
const OnLightRed = "\x1B[101m"
const OnLightYellow = "\x1B[103m"

// Styles ─────────────────────────── //

const Bold = "\x1B[1m"
const Blink = "\x1B[5m"
const Dimmed = "\x1B[2m"
const Italic = "\x1B[3m"
const Reversed = "\x1B[7m"
const Strikethrough = "\x1B[9m"
const Underline = "\x1B[4m"

// User Defined ───────────────────── //

const ERROR = Bold + LightRed
const INFO = LightGreen
const WARNING = Bold + LightYellow

const Annatate = LightGray
const Annote = Annatate
const Command = Bold + Yellow
const Var = Italic + LightMagenta
const Variable = Var

// Collections ────────────────────────────────────────────────────────────── //

func ArrayContains[T comparable](array []T, value T) bool {

    for _, item := range array {
        if item == value {
            return true
        }
    }

    return false
}

func MapContains[T comparable, U any](m map[T]U, key T) bool {
    _, exists := m[key]
    return exists
}

// Conversions ────────────────────────────────────────────────────────────── //

func IntToString(value int) string {
    return strconv.Itoa(value)
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

// Writes a slice of strings to a text file
func WriteLines(path string, lines []string) error {
    
    file, err := os.Create(path)
    if ReportOnError("Couldn't create file: "+path, err) {
        return err
    }

    defer file.Close()

    writer := bufio.NewWriter(file)
    for _, line := range lines {
        fmt.Fprintln(writer, line)
    }

    return writer.Flush()
}

func Write(path, contents string) error {

    file, err := os.Create(path)

    if ReportOnError("Error creating file", err) {
        return err
    }
    defer file.Close()

    _, err = file.WriteString(contents)

    ReportOnError("Error writing to file", err)
    return err
}

func WriteLinesToFile(path string, lines []string) error {
    return Write(path, strings.Join(lines, Newline))
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
    fmt.Println(ERROR + message + ResetColor)
}

func Heading(heading string) {

    prefix := "──  "
    formatted := prefix + heading + "  "

    count := CharacterCount(heading) + 6

    padded := formatted + strings.Repeat("─", HeadingWidth - count)

    fmt.Println(LightGreen + padded + ResetColor)
    fmt.Println()
}

func Info(message string) {
    fmt.Println(INFO + message + ResetColor)
}

func NL() {
    fmt.Println()
}

func ShortHeading(heading string) {

    prefix := "──  "
    formatted := prefix + heading + "  "

    count := CharacterCount(heading) + 6

    padded := formatted + strings.Repeat("─", ShortHeadingWidth - count)

    fmt.Println(LightGreen + padded + ResetColor)
    fmt.Println()
}

func Title(name string) {

    count := CharacterCount(name) + 4

    NL()
    // Line 1: Top border
    fmt.Print(Green)
    fmt.Println("┌─" + strings.Repeat("─", HeadingWidth - 4) + "─┐")

    // Line 2: Title with padding
    line := "│ " + name
    line = line + strings.Repeat(" ", HeadingWidth - count) + " │"
    fmt.Println(line)

    // Line 3: Bottom border
    fmt.Println("└─" + strings.Repeat("─", HeadingWidth - 4) + "─┘" + ResetColor)

    NL()
}

func Warn(message string) {
    fmt.Println(WARNING + message + ResetColor)
}

func Warning(message string) {
    fmt.Println(WARNING + message + ResetColor)
}