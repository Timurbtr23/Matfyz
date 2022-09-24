#!/bin/bash

set -ueo pipefail


default_out(){
    echo "load=$load kernel=$kernel cpus=$cpus"
}


load=$(cat /proc/loadavg | cut -d " " -f 1)
kernel=$(uname -r | cut -d "-" -f 1)
cpus=$(nproc)
help="Usage: sysinfo [options]
 -c   --cpu     Print number of CPUs.
 -l   --load    Print current load.
 -k   --kernel  Print kernel version.
 -s   --script  Each value on separate line.

Without arguments behave as with -c -l -k.

Copyright NSWI177 2022"

new_line=false


if [ $# -eq 0 ]; then
    default_out
    exit 0
fi

if [ $# -eq 1 ]; then
    default_out
    exit 0
fi


opts_short="lkchs"
opts_long="load,kernel,cpus,help,script"

# Check for bad usage first (notice the ||)
getopt -Q -o "$opts_short" -l "$opts_long" -- "$@"|| exit 1

# Actually parse them (we are here only if they are correct)
eval set -- "$( getopt -o "$opts_short" -l "$opts_long" -- "$@" )"


while [ $# -gt 0 ]; do
    case "$1" in
        -h|--help)
            echo "$help"
            exit 0
            ;;
        -l | --load)   echo -n "load=$load"     ;;
        -k | --kernel) echo -n "kernel=$kernel" ;;
        -c | --cpus)   echo -n "cpus=$cpus"     ;;
        -s | --script) new_line=true
    esac
    echo -n " "
    shift
done
