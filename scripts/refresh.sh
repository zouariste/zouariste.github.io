#!/bin/bash

if [[ "$1" == "--help" ]]; then
    echo "Usage: ./script.sh INPUT_FILE SERVER"
    echo "Refresh the input_file"
    exit 0
fi

input_file=$1
server=$2

if [ "$server" == "1" ]; then
    wget -c 'http://s.delta2022.xyz:8880/get/93077051//m3u_plus' && mv m3u* iptv.m3u
else
    wget -c 'http://s.delta2022.xyz:8880/get/94541124/57647818/m3u_plus' && mv m3u* iptv.m3u
fi


./extract_ids.sh $input_file
python3 extract_lines.py iptv.m3u generated_ids
rm generated_ids iptv.m3u
mv output_file $input_file
git add ../cv/ 
git commit -m "An update"
git push
