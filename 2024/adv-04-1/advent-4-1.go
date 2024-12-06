package main

// Answer: 2406

import (
	"fmt"
	"shared"
	"strings"
)

const Title = "Advent-04-1"

const (
	DataActual = "data-actual.txt"
	DataTest = "data-test.txt"
)

var Direction = []int{-1, 0, 1}
var Xmas = []rune{'X', 'M', 'A', 'S'}

// Data Block ─────────────────────────────────────────── //

type DataBlock struct {
	data [][]rune
	result [][]rune
}

func dimensions(dataBlock DataBlock) Vector {
	return Vector{len(dataBlock.data), len(dataBlock.data[0])}
}

func letterAt(dataBlock DataBlock, point Vector) rune {
	return dataBlock.data[point.y][point.x]
}

func updateLocation(dataBlock DataBlock, point Vector, letter rune) {
	dataBlock.result[point.y][point.x] = letter
}

// Vector ─────────────────────────────────────────────── //

type Vector struct {
	x int
	y int
}

type DirectionalPoint struct {
	point Vector
	direction Vector
}

func location(directionalPoint DirectionalPoint, index int) Vector {
	x := directionalPoint.point.x + directionalPoint.direction.x * index
	y := directionalPoint.point.y + directionalPoint.direction.y * index
	return Vector{x, y}
}


// Functions ─────────────────────────────────────────── //

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

func findXmas(lines []string) ([][]rune, int) {

	data := toRuneSlices(lines)

	findCount := 0

	for y, line := range data.data {
		for x, character := range line {
			if character == 'X' {
				point := Vector{x, y}
				findCount += findXmasAndUpdate(point, &data)
			}
		}

	}

	return data.result, findCount
}

func findXmasAndUpdate(point Vector, dataBlock *DataBlock) int {

	findCount := 0

	for _, x_direction := range Direction {
		for _, y_direction := range Direction {
			if x_direction == 0 && y_direction == 0 {
				continue
			}
			direction := Vector{x_direction, y_direction}
			directionalPoint := DirectionalPoint{point, direction}
			if findXmasInDirection(directionalPoint, dataBlock) {
				findCount++
			}
		}
	}

	return findCount
}

func findXmasInDirection(direction DirectionalPoint, dataBlock *DataBlock) bool {

	if isOutOfBounds(direction, dataBlock) {
		return false // can't have a match.
	}

	for index := 1; index < 4; index ++ {
		actual := location(direction, index)
		letter := Xmas[index]
		if letter != letterAt(*dataBlock, actual) {
			return false // nothing to do
		}
	}

	// Match

	for index := 0; index < 4; index ++ {
		actual := location(direction, index)
		letter := Xmas[index]
		updateLocation(*dataBlock, actual, letter)
	}	

	return true
}

func isOutOfBounds(direction DirectionalPoint, dataBlock *DataBlock) bool {

	bounds := location(direction, 3)
	size := dimensions(*dataBlock)

	if bounds.x < 0 || bounds.y < 0 {
		return true
	}

	if bounds.x >= size.x || bounds.y >= size.y {
		return true
	}

	return false
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

	print("Find Count: ", findCount)
	print()
	for _, line := range results {
		print(string(line))
	}
	print()
}