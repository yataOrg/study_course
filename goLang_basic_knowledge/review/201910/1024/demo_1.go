/*
* @Author: yanzhipeng
* @Date:   2019-10-24 18:14:14
* @Last Modified by:   yanzhipeng
* @Last Modified time: 2019-10-24 20:11:34
*/

package main

import (
	"net/http"
)

func main() {

	http.Handle("/", http.FileServer(http.Dir(".")))
	http.ListenAndServe(":8980", nil)
}