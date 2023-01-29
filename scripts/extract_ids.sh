#!/bin/bash

if [[ "$1" == "--help" ]]; then
    echo "Usage: ./script.sh INPUT_FILE"
    echo "Extracts the ids from the input file and writes them to a file named generated_ids"
    exit 0
fi

input_file=$1
string=$(cat $input_file)
echo "$string" | grep -oE '\/[0-9]+\.ts' | tr -d '/' | tr -d '.ts' > generated_ids

