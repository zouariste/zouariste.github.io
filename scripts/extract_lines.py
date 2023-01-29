import sys
import os
from urllib.parse import urlsplit

def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py INPUT_FILE IDS_FILE")
        print("Extracts the lines starting with '#' and the lines containing the specified ids followed by '.ts' from the input file and writes them to a file named output_file")
        return

    input_file = sys.argv[1]
    ids_file = sys.argv[2]

    # Read the ids from the ids file and store them in a dictionary
    ids_map = {}
    with open(ids_file, 'r') as f:
        for id in f:
            ids_map[id.strip()] = None

    prev_line_start_with_hash = False
    found_lines = 0
    extensions = (".ts", ".mp4", ".mkv")
    with open(input_file, 'r') as f:
        with open('output_file', 'w') as output_file:
            for line in f:
                url_parts = urlsplit(line)
                file_name = url_parts.path.split("/")[-1]
                
                id = os.path.splitext(file_name)[0]
                if (id != ''):  
                    for ext in extensions:
                        id = id.replace(ext, "")

                if id in ids_map:
                    if prev_line_start_with_hash:
                        output_file.write(prev_line)
                    output_file.write(line)
                    prev_line_start_with_hash = False
                    found_lines += 1
                    if found_lines == len(ids_map):
                        return
                if line.startswith('#'):
                    prev_line_start_with_hash = True
                    prev_line = line
                else:
                    prev_line_start_with_hash = False

if __name__ == '__main__':
    main()

