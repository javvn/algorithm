package main

import (
	"fmt"
	"strconv"
)

func main() {
	var f int
	var s string

	fmt.Scanln(&f)
	fmt.Scanln(&s)

	sum := 0

	for _, r := range s {
		i, _ := strconv.Atoi(string(r))

		sum += i

	}
	fmt.Println(sum)
}
