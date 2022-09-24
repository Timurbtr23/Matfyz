#!/bin/bash

cut -d: -f 3 </dev/stdin | sort -r -n | sed '2!d'
