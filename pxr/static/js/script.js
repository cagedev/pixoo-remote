
function toggleFullscreen() {
    if (!document.fullscreenElement) {
        document.documentElement.requestFullscreen()
            .then(() => { })
            .catch(err => {
                console.log(`An error occurred while trying to switch into fullscreen mode: ${err.message} (${err.name})`);
            });
    } else {
        document.exitFullscreen();
    }
}


// set event listeners
window.addEventListener('load', () => { 
    try {
        document.getElementById('fs-toggle').addEventListener('click', toggleFullscreen);
    } catch (e) {
        console.log(e);
    }
});
