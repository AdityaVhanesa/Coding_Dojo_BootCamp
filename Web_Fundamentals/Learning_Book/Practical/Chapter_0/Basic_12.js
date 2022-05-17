// Zero Negative nubmers

function zeroNegativeNumbers(arr){
    for (var i = 0; i < arr.length; i++){
        if ( arr[i] < 0){
            arr[i] = 0;
        }
    }
    return arr;
}

var test = [1, -10, -11, 12, 143523, -1341341];
zeroNegativeNumbers(test);
console.log(test);