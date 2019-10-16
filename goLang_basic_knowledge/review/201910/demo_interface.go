/*
* @Author: yanzhipeng
* @Date:   2019-10-14 22:58:21
* @Last Modified by:   yanzhipeng
* @Last Modified time: 2019-10-14 23:09:42
*/

package main

import (
	"fmt"
)

type Man interface {
	name() string
	age() int
}

type Woman struct {

}

func (woman Woman) name() string {

	return "xiao azhu"
}

func (woman Woman) age() int {

	return 23
}

type Peng struct {

}

func (peng Peng) name() string {

	return "xiao peng"
}

func (peng Peng) age() int {

	return 25
}

func main() {

	var man Man

	man = new(Woman)
	fmt.Println(man.name())
	fmt.Println(man.age())

	man = new(Peng)
	fmt.Println(man.name())
	fmt.Println(man.age())
}





