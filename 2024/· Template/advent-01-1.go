package main

// Rules
//

// Thoughts
//

// Answer: ?

import (
	"fmt"
	"shared"
)

const Title = "Advent-01-1"

const (
	DataActual = "data-actual.txt"
	DataTest = "data-test.txt"
)

func main() {

	print := fmt.Println

	shared.Title(Title)

	path := shared.SelectForTestOrActual(DataActual, DataTest)
	lines, _ := shared.ReadLinesWithoutCommentsBlanks(path)

	print()
}