// Write a function that sums the digits of number until that sum is only one digit.

function sumOfDigits(number){
    var sum = 0;
    while (true) {
        var digit = number % 10;
        number = Math.floor(number / 10);
        sum += digit;
        if ( number  == 0){
            break;
        }
    }
    return sum; 
}


function sumToOne(number){
    var sum = 0;
    while ( true ){
        sum = sumOfDigits(number);
        if ( Math.floor(sum / 10) == 0){
            break
        }
        number = sum;
    }

    console.log("Possible final one Digit sum --> " + sum);
    return sum;
}

sumToOne(777);