package main

import (
	"fmt"
	"shared"
	"sort"
	"strconv"
	"strings"
)

const (
	DataActual = "data-actual.txt"
	DataTest = "data-test.txt"
)

func diff(value1 int, value2 int) int {

	if value1 > value2 {
		return value1 - value2
	}

	return value2 - value1
}

func toInt(text string) int {

	value, err := strconv.Atoi(text)

	shared.ExitOnError("Couldn't convert to int: '" + text + "'", err)

	return value
}

func parseAndSort(lines []string) ([]int, []int) {

	var list1, list2 []int

	for _, line := range lines {

		items := strings.Fields(line)
		list1 = append(list1, toInt(items[0]))
		list2 = append(list2, toInt(items[1]))
	}

	sort.Ints(list1)
	sort.Ints(list2)

	return list1, list2
}

func main() {

	shared.Title("Advent 01 - 1")

	path := shared.SelectRunOption(DataActual, DataTest)

	lines, err := shared.ReadLines(path)
	shared.ExitOnError("Couldn't read: " + path, err)
	
	list1, list2 := parseAndSort(lines)

	sum := 0
	for i, item1 := range list1 {
		item2 := list2[i]
		sum += diff (item1, item2)
	}
	
	fmt.Println("Total:", sum)
}