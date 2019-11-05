/*
* @Author: yanzhipeng
* @Date:   2019-11-05 17:44:53
* @Last Modified by:   yanzhipeng
* @Last Modified time: 2019-11-05 17:51:09
*/

package main

import (
	"fmt"
)

type Flying struct {}

func (f *Flying) Fly() {
	fmt.Println("i can fly")
}

type Walkable struct {}

func (w *Walkable) Walk() {
	fmt.Println("i can walk")
}

type Human struct {
	Walkable
}

type Bird struct {
	Walkable
	Flying
}

func main() {

	b := new(Bird)
	fmt.Println("Bird: ")
	b.Fly()
	b.Walk()

	h := new(Human)
	fmt.Println("Human: ")
	h.Walk()
}