
// fullscreen toggle
window.addEventListener('click',
    () => {
        if (!document.fullscreenElement) {
            document.documentElement.requestFullscreen()
                .then(() => { })
                .catch(err => {
                    alert(`An error occurred while trying to switch into fullscreen mode: ${err.message} (${err.name})`);
                });
        } else {
            document.exitFullscreen();
        }
    }
);