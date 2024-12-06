package main

// Answer: 624

import (
	"fmt"
	"shared"
	"strings"
)

const Title = "Advent-02-2"

const (
	DataActual = "data-actual.txt"
	DataTest = "data-test.txt"
)


func isOutOfRange(diff int) bool {
	if diff < 0 {
		return diff > -1 || diff < -3
	}
	return diff < 1 || diff > 3
}

func isSafe(levels []int) bool {

	sign := toSign(levels[1] - levels[0])

	for i := 1; i < len(levels) ; i++ {

		diff := levels[i] - levels[i - 1]

		if isOutOfRange(diff) || isWrongSign(diff, sign) {
			return false
		}
	}

	return true
}

func isWrongSign(value int, sign int) bool {
	return value * sign < 0
}

func parse(lines []string) [][]int {

	var all [][]int

	for _, line := range lines {
		levels := strings.Fields(line)
		levelInts := shared.ToInts(levels)
		all = append(all, levelInts)
	}

	return all
}

func toSign(value int) int {
	if value >= 0 {
		return 1
	}
	return -1
}

func main() {

	shared.Title(Title)

	path := shared.SelectRunOption(DataActual, DataTest)

	lines, err := shared.ReadLines(path)
	shared.ExitOnError("Couldn't read: " + path, err)
	
	allLevels := parse(lines)

	sum := 0
	for _, levels := range allLevels {
		if isSafe(levels) {
			sum++
		}
	}
	
	fmt.Println("Total:", sum)
}