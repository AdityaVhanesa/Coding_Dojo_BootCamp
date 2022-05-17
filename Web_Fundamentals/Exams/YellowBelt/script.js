function cartEmptyAlert() {
    alert("Your Cart is empty!")
}

function changeImageToSucculents1(element) {
    element.style.backgroundImage = "url('images/succulents-1.jpg')";
}

function changeImageToSucculents2(element) {
    element.style.backgroundImage = "url('images/succulents-2.jpg')";
}

function acceptCookies(){
    var alertMsg = document.querySelector(".div-alert");
    alertMsg.remove();
}