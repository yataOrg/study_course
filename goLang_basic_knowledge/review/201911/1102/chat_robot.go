/*
* @Author: yanzhipeng
* @Date:   2019-11-02 08:27:50
* @Last Modified by:   yanzhipeng
* @Last Modified time: 2019-11-02 09:21:41
*/

package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {

	inputReader := bufio.NewReader(os.Stdin)
	fmt.Println("please input your name:")
	input, err := inputReader.ReadString('\n')
	if nil != err {
		fmt.Printf("there is has an error %s\n", err)
		os.Exit(1)
	}
	name := input[:len(input)-2]
	fmt.Printf("hello %s, what can i do for you", name)

	for {
		input, err := inputReader.ReadString('\n')
		fmt.Println(len(input), input)
		if nil != err {
			fmt.Printf("there is has an error %s\n", err)
			continue
		}
		if 1 == len(input) {
			fmt.Println("hello , what can i do for you")
			continue
		}
		input = input[:len(input)-2]
		input = strings.ToLower(input)

		switch input {
			case "":
				continue
			case "nothing", "bye":
				fmt.Println("bye!")
				os.Exit(1)
			default:
				fmt.Println("Sorry i can not catch you.")
		}


	}


}