var isTempUnitC = true;
function changeCity(cityName){
    alert("Loading Weather Report ... ");
    var selectedCity = document.querySelector(".bottom-main-container .bottom-top-row .city-name");
    selectedCity.innerText = cityName;
}

function acceptCookies(){
    var alertMsg = document.querySelector(".div-alert");
    alertMsg.remove();
}

function changeTempParameter(element){
    var value = element.value;
    if (value == "celcius" && isTempUnitC) {
        return;
    } else if (value == "celcius" && !isTempUnitC){
        changeAllValue("c");
        isTempUnitC = true;
        return;
    } else if (value == "fahrenheit" && !isTempUnitC){
        return;
    } else {
        changeAllValue("f");
        isTempUnitC = false;
        return;
    };
}

function convertToC(value){
    var value =  (value - 32 ) * 0.5556;
    return Math.round(value);
}

function convertToF(value){
    var value =  (value / 0.5556 ) + 32;
    return Math.round(value);
}

function changeAllValue(change){
    var maxTemp = document.querySelectorAll(".card .temp-row .max-temp");
    var minTemp = document.querySelectorAll(".card .temp-row .min-temp");
    if (change == "c"){
        console.log("Changing to Celcius")
        for(var i = 0; i < maxTemp.length; i++ ){
            maxTemp[i].innerText = convertToC(parseInt(maxTemp[i].innerText));
            minTemp[i].innerText = convertToC(parseInt(minTemp[i].innerText));
        };
    } else if (change == "f") {
        console.log("Changing to Fahrenheit")
        for(var i = 0; i < maxTemp.length; i++ ){
            maxTemp[i].innerText = convertToF(parseInt(maxTemp[i].innerText));
            minTemp[i].innerText = convertToF(parseInt(minTemp[i].innerText));
        };
    }
    
}