/*
* @Author: yanzhipeng
* @Date:   2019-10-15 07:31:53
* @Last Modified by:   yanzhipeng
* @Last Modified time: 2019-10-15 11:21:36
*/

package main

import "fmt"

func sum(s []int, c chan int) {

	sum := 0
	for _, v := range s {
		sum += v
	}
	c <- sum
}

func main() {

	s := []int {7, -3, 2, 5, 3, 9, 11, 44}
	c := make(chan int)
	go sum(s[len(s)/2:], c)
	go sum(s[:len(s)/2], c)

	x, y := <- c, <- c
	fmt.Println(x, y, x + y)