#!/bin/bash

input=$(</dev/stdin)

while read line; do 
	line=$(sed 's/AM//g' <<< $line)
	line=$(sed 's/PM//g' <<< $line)
	echo "$line" | sed -e "$( for i in 01 02 03 04 05 06 07; do echo "s:$i:$(( i + 12 )):g"; done )" 	 
done <<< "$input"

# grep '[0-9]' /dev/stdin

