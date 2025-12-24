import os

# --- Configuration ---
# Folder containing your album subfolders (e.g., music/Album One, music/Album Two)
music_dir = 'music'
output_html_file = 'index.html'

def find_cover_art(album_path):
    """Checks for common cover art filenames and returns the path if found."""
    for art_file in ['cover.jpg', 'folder.jpg', 'cover.png', 'folder.png']:
        potential_cover = os.path.join(album_path, art_file)
        if os.path.exists(potential_cover):
            # Ensure forward slashes for web paths
            return potential_cover.replace('\\', '/')
    return None

def generate_html():
    """Generates the main index.html file from the music directory."""
    html_content = f'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MZ's Player</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@24,400,0,0" />
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="app-container">
        <header>
            <h1>Mohamed Zouari's Library</h1>
        </header>
        
        <main id="album-list">
    '''

    # Sort albums alphabetically for a consistent order
    albums = sorted([d for d in os.listdir(music_dir) if os.path.isdir(os.path.join(music_dir, d))])
    
    if not albums:
        html_content += f'<p class="empty-state">No albums found in the "{music_dir}" directory.</p>'
    else:
        for album in albums:
            album_path = os.path.join(music_dir, album)
            cover_art_path = find_cover_art(album_path)
            
            # Album Card Structure
            html_content += f'''
            <div class="album-card">
                <div class="album-header">
                    <div class="album-art">
                        {'<img src="' + cover_art_path + '" alt="Cover for ' + album + '">' if cover_art_path else '<span class="material-symbols-outlined">album</span>'}
                    </div>
                    <div class="album-info">
                        <h2>{album}</h2>
                    </div>
                    <span class="material-symbols-outlined expand-icon">expand_more</span>
                </div>
                <ul class="song-list">
            '''
            
            # Sort songs and add them to the list
            songs = sorted([s for s in os.listdir(album_path) if s.lower().endswith('.mp3')])
            if not songs:
                html_content += '<li class="no-songs">No songs found in this album.</li>'
            else:
                for song in songs:
                    song_path = os.path.join(music_dir, album, song).replace('\\', '/')
                    song_title = os.path.splitext(song)[0] # Remove file extension for display
                    html_content += f'<li><a href="#" data-src="{song_path}">{song_title}</a></li>'
            
            html_content += '''
                </ul>
            </div>
            '''

    html_content += '''
        </main>

        <footer class="player-bar">
            <div id="now-playing">
                <span class="material-symbols-outlined">music_note</span>
                <p>Select a song to play</p>
            </div>
            <audio controls id="audio-player">
                Your browser does not support the audio element.
            </audio>
        </footer>
    </div>
    <script src="script.js"></script>
</body>
</html>
'''

    with open(output_html_file, 'w', encoding='utf-8') as file:
        file.write(html_content)
    print(f"'{output_html_file}' has been generated successfully! ✨")

# --- Main Execution ---
if __name__ == '__main__':
    if not os.path.exists(music_dir):
        os.makedirs(music_dir)
        print(f"Created '{music_dir}' directory. Please add your album folders with MP3 files inside.")
    else:
        generate_html()