// give the index, value and array insert the value in the array.

function insertAt(arr, index, value){
    var arrayLength = arr.length;
    if (index >= arrayLength){
        return
    } 

    var tempValue1 = arr[index];
    var tempValue2;
    arr[index] = value;
    for (var i = index+1; i < arrayLength; i++){
        tempValue2 = arr[i];
        arr[i] = tempValue1;
        tempValue1 = tempValue2;
    }
    arr[arrayLength] = tempValue1;
}

A = [0, 1, 3, 4, 5];
insertAt(A, 2, 2);
console.log(A);