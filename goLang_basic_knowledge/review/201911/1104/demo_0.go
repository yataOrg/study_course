package main

import (
    "fmt"
)

/*
type USB interface {
    Name() string
    Connect()
}
*/

type PhoncConnecter struct {
    name string
}

func (pc PhoncConnecter) Name() string {

	return pc.name

}

func (pc PhoncConnecter) Connect() {
    fmt.Println(pc.name)
}

func main() {
    // 第一种直接在声明结构时赋值
    /*
    var a USB
    a = PhoncConnecter{"PhoneC1"}
    fmt.Println(a.Name())
    a.Connect()
    */
   
    cc := PhoncConnecter{"PhoneC2"}
    cc.Connect()

}