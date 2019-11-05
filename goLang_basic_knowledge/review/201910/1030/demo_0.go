/*
* @Author: yanzhipeng
* @Date:   2019-10-30 07:21:16
* @Last Modified by:   yanzhipeng
* @Last Modified time: 2019-11-01 17:11:15
*/

package main

import (
	"fmt"
	"encoding/base64"
	"encoding/json"
)

func main() {

	var a [3]int = [3]int {1, 2, 3}
	var b [3]int = [3]int {1, 2, 4}
	c := [...]int {1, 2, 3}
	fmt.Println( a == b, a == c)

	var file_body_struct map[string]interface{}
	str1 := "eyJkdCI6W3siZmlsZSI6eyJtaWQiOiI1ZGJhNzZhZmVlOWVhYzE0ODQ2NGI5ODEiLCJuIjoidGFjdGljcy5nbyIsInMiOjMwMTMsIm1kNSI6ImMzNWU5ZGEyMWFhOThkMjkxZDE0N2M5NGMxMGY2MmQyIiwiZXh0IjoiZ28iLCJkbmwiOmZhbHNlLCJ0aXAiOiI8TE9XX1ZFUj4iLCJ3bSI6ZmFsc2V9fV0sInIiOnsiZyI6IkQwOTk1MzhCMjZCQjQ1MTQ4RkQxNEI0NTE2MTQyNzEyIiwidHMiOjE1NzI0OTY3MzgsInR5cGUiOiIxMyJ9LCJ1Ijp7ImQiOiJ3ZWJfaW0iLCJvdWlkIjoiMTc1OTM5NTIxMzQ5NzY0NzU2IiwidWlkIjoiMTc1OTM5NTIxMzQ5NzY0NzU2IiwiY2lkIjoiMTc1OTM5NTIxMzQ5NzY0NzU0IiwibiI6InBlbmcwIiwiYSI6IiJ9fQ=="
	msg_file_str, _ := base64.StdEncoding.DecodeString(str1)

	json.Unmarshal([]byte(msg_file_str), &file_body_struct)

	fmt.Printf("%+v", file_body_struct["dt"].([]interface{})[0].(map[string]interface{})["file"].(map[string]interface{})["mid"])

}