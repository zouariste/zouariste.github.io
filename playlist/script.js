document.addEventListener('DOMContentLoaded', function() {
    const audioPlayer = document.getElementById('audioPlayer');
    const songLinks = document.querySelectorAll('#albums a');

    songLinks.forEach(songLink => {
        songLink.addEventListener('click', function(event) {
            event.preventDefault();
            const songFile = this.getAttribute('data-file');
            audioPlayer.src = songFile;
            audioPlayer.play();
        });
    });
});

