#!/bin/bash

</dev/stdin tr -s ' ' | cut -d ' ' -f 2- | tr ' |' '+0'|tr -s '+'| bc
