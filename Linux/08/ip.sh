#!/bin/bash

input=$(</dev/stdin)
errors=$(grep 404 <<< "$input")

ip_address=$(echo "$errors" | awk '{print $1}' | sort | uniq -c | sort -r | head -n 1)
ip_address=$(echo ${ip_address[0]}) 

echo "$ip_address" | cut -d " " -f 2

