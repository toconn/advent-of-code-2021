package main

import (
	"fmt"
	"shared"
	"sort"
	"strings"
)

const Title = "Advent-01-2"

const (
	DataActual = "data-actual.txt"
	DataTest = "data-test.txt"
)

func countOccurences(items []int) map[int]int {

	counts := make(map[int]int)

	for _, item := range items {

		if mapHasEntry(counts, item) {
			counts[item] = counts[item] + 1
		} else {
			counts[item] = 1
		}
	}

	return counts
}

func mapHasEntry(map1 map[int]int, entry int) bool {
	_, exists := map1[entry]
	return exists
}

func parseAndSort(lines []string) ([]int, []int) {

	var list1, list2 []int

	for _, line := range lines {

		if shared.IsBlank(line) || shared.IsComment(line) {
			continue
		}

		items := strings.Fields(line)
		list1 = append(list1, shared.ToInt(items[0]))
		list2 = append(list2, shared.ToInt(items[1]))
	}

	sort.Ints(list1)
	sort.Ints(list2)

	return list1, list2
}

func main() {

	shared.Title(Title)

	path := shared.SelectRunOption(DataActual, DataTest)

	lines, err := shared.ReadLines(path)
	shared.ExitOnError("Couldn't read: " + path, err)
	
	list1, list2 := parseAndSort(lines)
	counts := countOccurences(list2)

	sum := 0
	for _, item := range list1 {
		if ! mapHasEntry(counts, item) {
			continue
		}
		count := counts[item]
		sum += item * count
	}
	
	fmt.Println("Total:", sum)
}