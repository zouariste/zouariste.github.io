#!/bin/bash
if [[ "$1" == "--help" ]]; then
    echo "Usage: ./script.sh INPUT_FILE IDS_FILE"
    echo "Extracts the lines starting with '#' and the lines containing the specified ids followed by '.ts' from the input file and writes them to a file named output_file"
    exit 0
fi

input_file=$1
ids_file=$2

# Create an associative array to store the ids
declare -A ids

# Read the ids from the ids file and store them in the array
while read -r id; do
    ids["$id"]=1
done < "$ids_file"

prev_line_start_with_hash=false
found_lines=0
while IFS= read -r line; do
    for id in "${!ids[@]}"; do
        if [[ $line =~ ^.*$id\.ts.* ]]; then
            if [ $prev_line_start_with_hash == true ]
            then
                echo "$prev_line" >> output_file
            fi
            echo "$line" >> output_file
            prev_line_start_with_hash=false
            found_lines=$((found_lines+1))
            if [ $found_lines -eq ${#ids[@]} ]
            then
                exit 0
            fi
            break
        fi
    done
    if [[ $line == \#* ]]; then
        prev_line_start_with_hash=true
        prev_line="$line"
    else
        prev_line_start_with_hash=false
    fi
done < "$input_file"

