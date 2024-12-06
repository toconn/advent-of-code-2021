package main

// Answer: 159892596

import (
	"fmt"
	"regexp"
	"shared"
	"strings"
)

const Title = "Advent-03-1"

const MultiplyExpression = `mul\(\d+\,\d+\)`

const (
	DataActual = "data-actual.txt"
	DataTest = "data-test.txt"
)

func calcInstruction(instruction string) int {

	values := strings.TrimSuffix(
		strings.TrimPrefix(instruction, "mul("),
		")")

	parts := strings.Split(values, ",")
	ints := shared.ToInts(parts)

	return ints[0] * ints[1]
}

func extractInstructions(line string) []string {

	regex := regexp.MustCompile(MultiplyExpression)
	return regex.FindAllString(line, -1)
}


func extractLinesInstructions(lines []string) []string {

	var instructions []string
	
	for _, line := range lines {
		current := extractInstructions(line)
		instructions = append(instructions, current...)
	}

	return instructions
}

func main() {

	shared.Title(Title)

	path := shared.SelectRunOption(DataActual, DataActual)

	lines, err := shared.ReadLinesWithoutCommentsBlanks(path)
	shared.ExitOnError("Couldn't read: " + path, err)
	
	instructions := extractLinesInstructions(lines)

	for _, instruction := range instructions {
		fmt.Println(instruction)
	}

	sum := 0
	for _, instructions := range instructions {
		value := calcInstruction(instructions)
		sum += value
	}

	fmt.Println("Sum: ", sum)
}