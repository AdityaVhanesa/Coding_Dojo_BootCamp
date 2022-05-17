function playVideo(element){
    element.muted = true;
    element.play();
    console.log("Playing Video")
}

function pauseVideo(element){
    element.pause();
}