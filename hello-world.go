package main

import "fmt"

func main() {
	fmt.Println("Build from commit: $CODEBUILD_RESOLVED_SOURCE_VERSION")
	fmt.Println("hello world")
}