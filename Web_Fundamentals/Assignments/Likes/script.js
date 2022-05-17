function likeButton(element){
    var like = document.querySelector("#likes");
    var num = parseInt(like.innerText);
    like.innerText = num + 1;
}
