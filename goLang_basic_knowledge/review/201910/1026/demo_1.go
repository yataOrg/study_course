/*
* @Author: yanzhipeng
* @Date:   2019-10-26 08:10:56
* @Last Modified by:   yanzhipeng
* @Last Modified time: 2019-10-27 07:22:34
*/

package main

import (
	"fmt"
	"runtime"
	"math"
)

func init() {

	fmt.Printf("Map %v\n", m)
	info = fmt.Sprintf("OS: %s, Arch: %s", runtime.GOOS, runtime.GOARCH)
}

var m = map[int]string{1: "A", 2: "B", 3: "C"}

var info string

func main() {
	fmt.Println(info)
	fmt.Println(math.MaxFloat32)
	fmt.Println(math.MaxFloat64)
}