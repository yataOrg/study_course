/*
* @Author: yanzhipeng
* @Date:   2019-10-15 08:03:15
* @Last Modified by:   yanzhipeng
* @Last Modified time: 2019-10-15 08:07:50
*/

package main

import (
	"fmt"
)

func main() {

	c := make(chan int, 2)
	c <- 2
	c <- 3
	fmt.Println(<- c)
	c <- 1

	fmt.Println(<- c)
	fmt.Println(<- c)
}