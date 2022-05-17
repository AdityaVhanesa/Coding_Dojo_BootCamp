function reverseArray(arr){
    var arrayLength = arr.length;
    var numberOfLoop;
    if(arrayLength % 2 == 0){
        numberOfLoop = arrayLength / 2;
    } else {
        numberOfLoop = (arrayLength + 1) / 2;
    }
    for (var i = 0; i < numberOfLoop; i++ ){
        var temp = arr[i];
        arr[i] = arr[arrayLength - 1 - i];
        arr[arrayLength - 1 - i ] = temp;
    }
}

A = [1, 2, 3, 4];
reverseArray(A);
console.log(A);