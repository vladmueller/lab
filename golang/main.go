package main

import (
	"errors"
	"fmt"
	"os"
)

func main() {
	a := float64(42)
	b := float64(0)

	result, err := divide(a, b)
	if err != nil {
		fmt.Println("Division by zero is not allowed:", err)
		os.Exit(1)
	}

	fmt.Println(result)
}

// NOTE: a function in Go can return multiple return values

func divide(left float64, right float64) (float64, error) {
	if right == 0 {
		return 0, errors.New("division by zero")
	}

	return left / right, nil
}
