#!/bin/bash

set -ueo pipefail

tmpinputfile=$(mktemp /tmp/sctemp.XXXXXXXXXX)
echo "$(</dev/stdin)" > $tmpinputfile

declare -A teams


while read line; do
    data=($line)
    team=${data[0]}
    score=${data[1]}

    if [ ! -v teams[$team] ]; then
        teams[$team]=$score
    else
        teams[$team]=$(( teams[$team] + $score ))
    fi
done < $tmpinputfile

tmpreadyfile=$(mktemp /tmp/scrtemp.XXXXXXXXXX)

for team in "${!teams[@]}"; do
    echo "$team:${teams[$team]}" >> $tmpreadyfile
done

sort $tmpreadyfile

rm "$tmpinputfile"
rm "$tmpreadyfile"
