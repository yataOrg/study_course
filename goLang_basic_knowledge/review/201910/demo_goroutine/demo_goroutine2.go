/*
* @Author: yanzhipeng
* @Date:   2019-10-23 21:24:14
* @Last Modified by:   yanzhipeng
* @Last Modified time: 2019-10-24 18:12:57
*/

package main

import (
	"fmt"
	"math/rand"
	"time"
)

// 数据生产者
func producer(header string, channel chan<- string) {

	for {
		channel <- fmt.Sprintf("%s: %v", header, rand.Int31())
		time.Sleep(time.Second)
	}
}

// 数据消费者
func customer(channel <-chan string) {

	for {
		// 从channel中取出数据，此处会阻塞直到信道中返回数据
		message := <-channel
		fmt.Println(message)
	}
}

func main() {

	channel := make(chan string)
	go producer("azhu", channel)
	go producer("apeng", channel)
	go producer("apeng1111", channel)

	// 数据消费函数
	go customer(channel)
	customer(channel)
}




