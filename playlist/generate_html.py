import os

# Define paths
music_dir = 'music'  # Folder containing album subfolders
output_html_file = 'index.html'

# Create the HTML structure
def generate_html():
    html_content = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Music Player</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="music-player">
        <div id="albums">
    '''

    # Traverse directory
    for album in os.listdir(music_dir):
        album_path = os.path.join(music_dir, album)
        if os.path.isdir(album_path):
            html_content += f'<div class="album"><h2>{album}</h2><ul>'
            for song in os.listdir(album_path):
                if song.endswith('.mp3'):
                    song_path = f'{music_dir}/{album}/{song}'
                    html_content += f'<li><a href="{song_path}" data-file="{song_path}">{song}</a></li>'
            html_content += '</ul></div>'

    html_content += '''
        </div>
        <audio controls id="audioPlayer">
            Your browser does not support the audio element.
        </audio>
    </div>
    <script src="script.js"></script>
</body>
</html>
'''

    with open(output_html_file, 'w') as file:
        file.write(html_content)
    print('HTML file has been generated!')

# Run the function
generate_html()
