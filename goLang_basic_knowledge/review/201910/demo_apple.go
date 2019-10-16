/*
* @Author: yanzhipeng
* @Date:   2019-10-14 23:35:23
* @Last Modified by:   yanzhipeng
* @Last Modified time: 2019-10-14 23:50:40
*/

package main

import (
	"fmt"
)

type fruit interface {
	getName() string
	setName(name string) string
}

type apple struct {
	name string
}

func (a *apple) getName() string {
	return a.name
}

func (a *apple) setName(name string) string {
	a.name = name
	return name
}

func main() {

	a := apple{"红富士"}
	fmt.Println(a.getName())
	a.setName("树顶红")
	fmt.Println(a.getName())
}