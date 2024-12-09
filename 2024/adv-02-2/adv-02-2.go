package main

// Answer: 658

import (
	"fmt"
	"shared"
	"strings"
)

const Title = "Advent-02-2"

const (
	AllowFault = true
	FailOnFault = false
)

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

func isSafe(levels []int, allowFault bool) (bool, int) {

	sign := toSign(levels[1] - levels[0])

	for i := 1; i < len(levels); i++ {

		diff := levels[i] - levels[i - 1]

		if isOutOfRange(diff) || isWrongSign(diff, sign) {

			if ! allowFault {
				return false, i
			}

			// for j := i - 1; j < len(levels); j++ {
			for j := 0; j < len(levels); j++ {
				safe, _ := isSafe(split(levels, j), FailOnFault)
				if safe {
					return true, j
				}
			}
			return false, i
		}		
	}

	return true, -1
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

func printLevel(level []int, safe bool, faultIndex int) {

	if safe {
		fmt.Print("✅ ")
	} else {
		fmt.Print("🚫 ")
	}
	
	for index, value := range level {
		if index == faultIndex {
			fmt.Printf(" %s%2d%s", shared.LightRed, value, shared.Reset)
		} else {
			fmt.Printf(" %2d", value)
		}
	}

	fmt.Println()
}

func split(slice []int, index int) []int {

	before := append([]int(nil), slice[:index]...)
	after := append([]int(nil), slice[index+1:]...)
	return append(before, after...)
}

func toSign(value int) int {

	if value >= 0 {
		return 1
	}
	return -1
}

func main() {

	shared.Title(Title)

	path := shared.SelectForTestOrActual(DataActual, DataTest)

	lines, _ := shared.ReadLines(path)
	lines = shared.RemoveCommentsAndBlanks(lines)
	
	allLevels := parse(lines)

	sum := 0
	for _, levels := range allLevels {

		safe, index := isSafe(levels, AllowFault)
		printLevel(levels, safe, index)
		if safe {
			sum++
		}
	}
	fmt.Println()
	
	fmt.Println("Total:", sum)
}