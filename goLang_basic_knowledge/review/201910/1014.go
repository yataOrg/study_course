/*
* @Author: yanzhipeng
* @Date:   2019-10-14 07:45:06
* @Last Modified by:   yanzhipeng
* @Last Modified time: 2019-10-16 17:13:43
*/

package main
import "fmt"

func main() {

	var numbers = make([]int, 3, 5)
	var numbers1 []int
	printSlice(numbers)
	printSlice(numbers1)

	// var c []int
	aaa := []int{1, 2}
	aaa1 := aaa[len(aaa):]
	fmt.Println(len(aaa))
	fmt.Println(len(aaa1))

}

func printSlice(x []int) {

	fmt.Printf("len=%d cap=%d slice=%v \n", len(x), cap(x), x)
}