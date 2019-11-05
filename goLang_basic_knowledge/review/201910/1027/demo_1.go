/*
* @Author: yanzhipeng
* @Date:   2019-10-27 07:38:00
* @Last Modified by:   yanzhipeng
* @Last Modified time: 2019-10-27 07:52:11
*/

package main

import (
	"image"
	"image/color"
	"image/png"
	"log"
	"math"
	"os"
)

func main() {

	const size = 300
	pic := image.NewGray(image.Rect(0, 0, size, size))

	for x := 0; x < size; x++ {
		for y := 0; y < size; y++ {
			pic.SetGray(x, y, color.Gray{255})
		}
	}

	for x := 0; x < size; x++ {
		s := float64(x) * 2 * math.Pi / size
		y := size / 2 - math.Sin(s) * size  / 2
		// 用黑色绘制sin的轨迹
		pic.SetGray(x, int(y), color.Gray{0})
	}

	file, err := os.Create("sin.png")
	if nil != err {
		log.Fatal(err)
	}
	png.Encode(file, pic)
	file.Close()
}