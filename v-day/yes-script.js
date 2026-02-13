let musicPlaying = false

window.addEventListener('load', () => {
    launchConfetti()

    const music = document.getElementById('bg-music')
    music.volume = 0
    music.play().then(() => {
        fadeInMusic(music)
        musicPlaying = true
    }).catch(() => {})

    // Cinematic reveal
    setTimeout(() => {
        document.getElementById('love-reveal').classList.add('show')
    }, 1800)
})

function fadeInMusic(music) {
    let volume = 0
    const interval = setInterval(() => {
        if (volume >= 0.3) {
            clearInterval(interval)
        } else {
            volume += 0.02
            music.volume = volume
        }
    }, 100)
}

function launchConfetti() {
    const colors = ['#ff69b4', '#ff1493', '#ff85a2', '#ffb3c1', '#ff0000', '#ff6347', '#fff', '#ffdf00']
    const duration = 6000
    const end = Date.now() + duration

    confetti({
        particleCount: 150,
        spread: 100,
        origin: { x: 0.5, y: 0.3 },
        colors
    })

    const interval = setInterval(() => {
        if (Date.now() > end) {
            clearInterval(interval)
            return
        }

        confetti({
            particleCount: 40,
            angle: 60,
            spread: 55,
            origin: { x: 0, y: 0.6 },
            colors
        })

        confetti({
            particleCount: 40,
            angle: 120,
            spread: 55,
            origin: { x: 1, y: 0.6 },
            colors
        })
    }, 300)
}

function toggleMusic() {
    const music = document.getElementById('bg-music')

    if (musicPlaying) {
        music.pause()
        musicPlaying = false
        document.getElementById('music-toggle').textContent = '🔇'
    } else {
        music.play()
        musicPlaying = true
        document.getElementById('music-toggle').textContent = '🔊'
    }
}
