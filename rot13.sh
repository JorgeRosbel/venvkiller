#!/bin/bash

set -o pipefail

rot13() {
    if [ "$2" == "-d" ]; then
        cat $1 | tr 'N-ZA-Mn-za-m' 'A-Za-z'
    elif [ "$2" == "-e" ]; then
        cat $1 | tr 'A-Za-z' 'N-ZA-Mn-za-m'
    else
        echo "Usage: rot13 <file> <option>"
        echo "Options:"
        echo "  -d  Decode"
        echo "  -e  Encode"
        exit 1
    fi
}

rot13 $1 $2

