/*
* @Author: yanzhipeng
* @Date:   2019-10-12 08:29:50
* @Last Modified by:   yanzhipeng
* @Last Modified time: 2019-10-12 08:36:40
*/

package main

import (
	"fmt"
)

func init() {

}

func main() {

	const (
		a = iota
		b
		c
		d = "ha"
		e
		f = 100
		g
		h = iota
		i 
	)
	fmt.Println(a, b, c, d, e, f, g, h, i)

	const (
		e1 = ""
		a1 = "azhu"
		b1
		c1
		d1
	)
	fmt.Println(e1, a1, b1, c1, d1)
	const bbb int = 4
	fmt.Println(bbb)
}
