function changeProfile(){
    document.querySelector(".user-bottom-container h1").innerText = "Aditya Vhanesa";
}

function declineRequest(connectionName){
    var connections = document.querySelectorAll(".connection-container");
    for(var i = 0; i < connections.length; i++){
        var connection = connections[i];
        var requestNumber = document.querySelector(".side-container .side-top-container .request-number");
        var number = parseInt(requestNumber.innerText);
        var tempName = connection.querySelector(".connection-name").innerText;
        if (tempName == connectionName){
            connection.remove();
            requestNumber.innerText = number - 1;
            return
        }
    }
}