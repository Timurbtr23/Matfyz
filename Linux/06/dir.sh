#!/bin/bash

set -ueo pipefail

dirpath=$@

if [ $# -eq 0 ]; then
    dirpath=*
fi

for entry in $dirpath
do
	if test -e "$entry"; then
		if test -f "$entry"; then
			FILESIZE=$(stat -c%s "$entry")
			echo "$entry $FILESIZE"

		elif test -d "$entry"; then
			echo "$entry <dir>"

		else
			echo "$entry <special>"
		fi
	else
		echo "$entry: no such file or directory.">&2
	fi
done | column --table --table-noheadings --table-columns FILENAME,SIZE --table-right SIZE
