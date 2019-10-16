/*
* @Author: yanzhipeng
* @Date:   2019-10-15 07:16:56
* @Last Modified by:   yanzhipeng
* @Last Modified time: 2019-10-15 07:22:12
*/

package main

import (
	"fmt"
	"time"
)

func say(s string) {
	for i := 0; i < 5; i ++ {
		time.Sleep(100 * time.Millisecond)
		fmt.Println(s)
	}
}

func main() {
	go say("azhu")
	say("i love you and you love me")
}

