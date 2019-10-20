# @Author: yanzhipeng
# @Date:   2019-10-16 22:23:51
# @Last Modified by:   yanzhipeng
# @Last Modified time: 2019-10-17 07:31:20

#!/bin/bash

echo "hello world!"

your_name="azhu"

your_name="azhu1"
echo $your_name
echo {$your_name}

myUrl="https://google.com"
readonly myUrl
# myUrl="ddd"
unset your_name
echo $your_name

string="hello world"
echo ${#string}
echo ${string:1:4}

# echo `expr index "$string" io`

azhu3="https://github.com/ppker"
echo ${azhu3#*//}
echo ${azhu3##*/}

echo ${azhu3%/*}
echo ${azhu3%/*}
echo ${azhu3%%/*}

echo ${azhu3:0:6}
echo ${azhu3:1}

echo ${azhu3:0-7:2}
echo ${azhu3:0-7}

expr length azhu3

