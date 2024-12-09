package main

// Rules
// 1. Pages must be ordered according to the rule lower | upper
// 2. Find all pages out of order.
// 3. Fix the order according to the rule.

// Thoughts
//

// Answer: ?

import (
	"fmt"
	"shared"
	"strings"
)

const Title = "Advent-05-2"

const (
	DataActual = "data-actual.txt"
	DataTest = "data-test.txt"
)

// Types ──────────────────────────────────────────────────────────────────── //

type CompareRule struct {
	lower int
	upper int
}

func (compare CompareRule) String() string {
	return fmt.Sprintf("%d | %d", compare.lower, compare.upper)
}


type Rules struct {
	rulesMap map[int][]int
}

func (rules Rules) hasUpperInMap(lower int, numbersMap map[int]bool) (bool, int) {
	for _, upper := range rules.uppers(lower) {
		if numbersMap[upper] {
			return true, upper
		}
	}
	return false, -1
}

func (rules Rules) hasRule(number int) bool {
	_, exists := rules.rulesMap[number]
	return exists
}

func (rules Rules) uppers(lower int) []int {
	return rules.rulesMap[lower]
}

// Parsing ────────────────────────────────────────────────────────────────── //

func isRule(line string) bool {
	return strings.Contains(line, "|")
}

func parse(lines []string) (*[]CompareRule, *[][]int) {

	var rules []CompareRule
	var sortList [][]int

	for _, line := range lines {
		if isRule(line) {
			rules = append(rules, toRule(line))
		} else {
			sortList = append(sortList, toValues(line))
		}
	}

	return &rules, &sortList
}

func toRule(line string) CompareRule {
	parts := strings.Split(line, "|")
	lower, upper := shared.ToInt(parts[0]), shared.ToInt(parts[1])
	return CompareRule{lower, upper}
}

func toValues(line string) []int {
	return shared.ToInts(strings.Split(line, ","))
}

// Sorting ────────────────────────────────────────────────────────────────── //

func notInOrder(numbers []int, rules *Rules) (bool, int, CompareRule) {

	numberMap := make(map[int]bool)

	for index, number := range numbers {
		if rules.hasRule(number) {
			hasUpper, value := rules.hasUpperInMap(number, numberMap)
			if hasUpper {
				return true, index, CompareRule{number, value}
			}
		}
		numberMap[number] = true
	}
	return false, -1, CompareRule{0, 0}
}

func swap

func toRules(rules *[]CompareRule) *Rules {

	rulesMap := make(map[int][]int)

	for _, rule := range *rules {
		if shared.MapContains(rulesMap, rule.lower) {
			rulesMap[rule.lower] = append(rulesMap[rule.lower], rule.upper)
		} else {
			rulesMap[rule.lower] = []int{rule.upper}
		}
	}

	return &Rules{rulesMap}
}

// Main ────────────────────────────────────────────────────────────────────── //

func printList(numbers []int, inOrder bool, index int, rule CompareRule) {	

	var buffer strings.Builder

	if inOrder {
		buffer.WriteString("✅  ")
		buffer.WriteString(fmt.Sprintf("%s%2d%s      ", shared.Green, numbers[index], shared.Reset))

	} else {
		buffer.WriteString("🚫  ")
		buffer.WriteString(fmt.Sprintf("%s%2d | %2d%s ", shared.WARNING, rule.lower, rule.upper, shared.Reset))
	}

	for i, number := range numbers {
		if i == index {
			if inOrder {
				buffer.WriteString(fmt.Sprintf(" %s%2d%s", shared.White + shared.Bold, number, shared.Reset))
			} else {
				buffer.WriteString(fmt.Sprintf(" %s%2d%s", shared.WARNING, number, shared.Reset))
			}
		} else {
			buffer.WriteString(fmt.Sprintf(" %2d", number))
		}
	}

	fmt.Println(buffer.String())
}


func main() {

	print := fmt.Println

	shared.Title(Title)

	path := shared.SelectForTestOrActual(DataActual, DataTest)

	lines, err := shared.ReadLinesWithoutCommentsBlanks(path)
	shared.ExitOnError("Couldn't Read data file: '" + path + "'", err)

	ruleList, sortList := parse(lines)
	rules := toRules(ruleList)

	sum := 0
	for _, numbers := range *sortList {
		inOrder, index, rule := notInOrder(numbers, rules)
		printList(numbers, inOrder, index, rule)
	}

	print()
	print("Sum:", sum)
	print()
}