document.addEventListener('DOMContentLoaded', () => {
    const albumList = document.getElementById('album-list');
    const audioPlayer = document.getElementById('audio-player');
    const nowPlayingEl = document.querySelector('#now-playing p');
    let currentPlayingLink = null;

    if (!albumList) return;

    albumList.addEventListener('click', (event) => {
        const header = event.target.closest('.album-header');
        const songLink = event.target.closest('.song-list a');

        // --- Handle Album Toggle ---
        if (header) {
            const card = header.closest('.album-card');
            if (card) {
                card.classList.toggle('active');
            }
            return;
        }

        // --- Handle Song Click ---
        if (songLink) {
            event.preventDefault(); // Prevent page from reloading
            
            const songSrc = songLink.getAttribute('data-src');
            
            // Update audio source and play
            audioPlayer.src = songSrc;
            audioPlayer.play();

            // Update "Now Playing" display
            nowPlayingEl.textContent = songLink.textContent;

            // Remove highlight from the previously playing song
            if (currentPlayingLink) {
                currentPlayingLink.classList.remove('playing');
            }
            // Add highlight to the new song
            songLink.classList.add('playing');
            currentPlayingLink = songLink;
        }
    });

    // Remove highlight when the song ends
    audioPlayer.addEventListener('ended', () => {
        if (currentPlayingLink) {
            currentPlayingLink.classList.remove('playing');
            currentPlayingLink = null;
        }
        nowPlayingEl.textContent = "Select a song to play";
    });
});