/*
* @Author: yanzhipeng
* @Date:   2019-10-15 08:11:02
* @Last Modified by:   yanzhipeng
* @Last Modified time: 2019-10-15 08:20:47
*/

package main

import (
	"fmt"
)

func fibonacci(n int, c chan int) {

	x, y := 0, 1
	for i := 0; i < n; i++ {
		c <- x
		x, y = y, x + y
	}
	close(c)
}

func main() {

	c := make(chan int, 10)
	go fibonacci(cap(c), c)

	for i := range c {
		fmt.Println(i)
	}
}