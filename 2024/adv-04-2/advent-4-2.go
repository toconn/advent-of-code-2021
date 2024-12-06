package main

// Answer: 1807

import (
	"fmt"
	"shared"
	"strings"
)

const Title = "Advent-04-2"

const (
	DataActual = "data-actual.txt"
	DataTest = "data-test.txt"
)

var offsets = []Vector{
	{-1, -1},
	{1, -1},
	{-1, 1},
	{1, 1},
}

// Data Block ─────────────────────────────────────────── //

type DataBlock struct {
	data [][]rune
	result [][]rune
}

func (dataBlock DataBlock) dimensions() Vector {
	return Vector{len(dataBlock.data), len(dataBlock.data[0])}
}

func (dataBlock DataBlock) letterAt(point Vector) rune {
	return dataBlock.data[point.y][point.x]
}

func (dataBlock DataBlock) letterToResult(point Vector) {
	dataBlock.updateLocation(point, dataBlock.letterAt(point))
}

func (dataBlock DataBlock) updateLocation (point Vector, letter rune) {
	dataBlock.result[point.y][point.x] = letter
}

// Vector ─────────────────────────────────────────────── //

type Vector struct {
	x int
	y int
}

func add (point Vector, offset Vector) Vector {
	return Vector{point.x + offset.x, point.y + offset.y}
}

func (point Vector) invert() Vector {
	return Vector{- point.x, - point.y}
}

// Functions ─────────────────────────────────────────── //

func isMas(dataBlock DataBlock, point Vector, offset Vector) bool {

	return dataBlock.letterAt(add(point, offset)) == 'M' &&
		dataBlock.letterAt(add(point, offset.invert())) == 'S'
}

func findXmas(lines []string) ([][]rune, int) {

	data := toRuneSlices(lines)
	dimensions := data.dimensions()

	findCount := 0

	for y := 1; y < dimensions.y - 1; y++ {
		for x := 1; x < dimensions.x - 1; x++ {

			point := Vector{x, y}
			character := data.letterAt(point)

			if character == 'A' {
				if isXmas(&data, point) {
					update(&data, point)
					findCount++
				}
			}
		}
	}

	return data.result, findCount
}

func isXmas(dataBlock *DataBlock, point Vector) bool {

	count := 0

	for _, offset := range offsets {
		if isMas(*dataBlock, point, offset) {
			count++
		}
	}

	return count == 2
}

func toRuneSlices(lines []string) DataBlock {

	data := make([][]rune, len(lines))
	result := make([][]rune, len(lines))

	for i, line := range lines {
		runes := []rune(line)
		result[i] = []rune(strings.Repeat(".", len(runes)))
		data[i] = runes
	}

	return DataBlock{data, result}
}

func update(dataBlock *DataBlock, point Vector) {

	dataBlock.letterToResult(point)
	for _, offset := range offsets {
		dataBlock.letterToResult(add(point, offset))
	}
}

func main() {

	print := fmt.Println

	shared.Title(Title)

	path := shared.SelectRunOption(DataActual, DataTest)

	lines, err := shared.ReadLinesWithoutCommentsBlanks(path)
	shared.ExitOnError("Couldn't read: " + path, err)

	for _, line := range lines {
		print(string(line))
	}
	print()


	results, findCount := findXmas(lines)

	for _, line := range results {
		print(string(line))
	}
	print()
	print("Find Count: ", findCount)
	print()
}