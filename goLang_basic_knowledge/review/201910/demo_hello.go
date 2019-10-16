/*
* @Author: yanzhipeng
* @Date:   2019-10-11 17:43:27
* @Last Modified by:   yanzhipeng
* @Last Modified time: 2019-10-13 08:48:37
*/

package main

import (
	"fmt"
	"strings"
	"unsafe"
)

func init() {

	fmt.Print("小哆哆 来啦 \n")
}


func main() {

	fmt.Println("Hello World!" + " azhu")
	var a = 1
	var b float64 = 1.5
	fmt.Println(a, b)

	test_str := "azhu www\n.azhu\n.com"
	fmt.Println("this origin string is " + test_str)
	now_str := strings.Replace(test_str, " ", "", -1)
	fmt.Println("去空格后的字符串为 " + now_str)
	now_str = strings.Replace(now_str, "\n", "", -1)
	fmt.Println("最后的字符串为 " + now_str)

	var dd int
	dd, bb := 1, 2
	fmt.Printf("%v %v\n", dd, bb)

	azhu := "hello1"
	fmt.Println(unsafe.Sizeof(azhu))

	var azhu2 *int
	var azhu3 int = 3
	azhu2 = &azhu3
	fmt.Println(azhu2)
	fmt.Println(*azhu2)

	var balance [10] float32
	var balance1 = [5] float32 {100.0, 2.2, 1.343, 3.0, 21.3}
	// var balance2 = [...]float32 {1.1, 1.23, 1.241}
	var balance3 = [...]float32 {1.2, 1.34, 1.445}

	fmt.Printf("--- %T\n --- %T\n --- %T\n", balance, balance1, balance3)

}





