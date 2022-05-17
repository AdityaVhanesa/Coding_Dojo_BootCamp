// Square the vales
function squareArrayValues(arr){
    for ( var i = 0; i < arr.length; i++){
        var value = arr[i];
        arr[i] = value * value;
    }
}

var A = [1,2,3,4];
squareArrayValues(A);
console.log(A);