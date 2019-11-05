/*
* @Author: yanzhipeng
* @Date:   2019-11-04 21:21:40
* @Last Modified by:   yanzhipeng
* @Last Modified time: 2019-11-04 21:21:44
*/

package main
import (
    "fmt"
    "time"
)
const LIM = 41
var fibs [LIM]uint64
func main() {
    var result uint64 = 0
    start := time.Now()
    for i := 0; i < LIM; i++ {
        result = fibonacci(i)
        fmt.Printf("fibonacci(%d) is: %d\n", i, result)
    }
    end := time.Now()
    delta := end.Sub(start)
    fmt.Printf("longCalculation took this amount of time: %s\n", delta)
}
func fibonacci(n int) (res uint64) {
    // 记忆化：检查数组中是否已知斐波那契（n）
    if fibs[n] != 0 {
        res = fibs[n]
        return
    }
    if n <= 1 {
        res = 1
    } else {
        res = fibonacci(n-1) + fibonacci(n-2)
    }
    fibs[n] = res
    return
}