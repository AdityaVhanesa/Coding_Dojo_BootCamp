// 
function lastDigitOfAToTheB(number1, number2){
    var result = 1;
    for (var i = 0; i < number2; i++){
        result *= number1;
    }
    return result % 10;
}

console.log(lastDigitOfAToTheB(123, 5));