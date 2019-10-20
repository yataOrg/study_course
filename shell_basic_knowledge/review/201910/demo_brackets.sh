# @Author: yanzhipeng
# @Date:   2019-10-17 08:02:49
# @Last Modified by:   yanzhipeng
# @Last Modified time: 2019-10-17 08:17:32

#!/bin/bash
#
fpath="/etc/passwd"
if [ -e $fpath ]; then
	echo File exist;
else
	echo Does not exist;
fi

azhu0="azhu0"
azhu1="azhu1"


azhu2="True"
azhu3=""

if [[ -n $azhu2 ]] && [[ -z $azhu3 ]]; then
	echo "azhu2 = ${azhu2}  azhu3 = ${azhu3}"
fi

if test $azhu0 = "azhu0"; then echo "True"; fi