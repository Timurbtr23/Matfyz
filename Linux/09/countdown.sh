#!/bin/bash

set -ueo pipefail

start=$1

on_exit() {
    echo -e "\nAborted"
    sleep 1
    trap - EXIT
    exit 17
}

trap "on_exit" INT TERM

while [ "$start" -gt 0 ];
do
	echo "$start"
	start=$(( start - 1 ))
	sleep 1
done
