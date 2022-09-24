#!/bin/bash

( ( test -f .NO_HEADER || ( test -f HEADER && cat HEADER ) ) && exit 0) || 
	( echo "Error: HEADER not found.">&2 && exit 1 ) 
