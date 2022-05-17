//Remove the value from the begining of the array  Do this
// without using any built-in array methods.

function popAtFront(arr){
    if (arr.length == 1){
        return arr.pop();
    }
    var tempValue1 = arr[arr.length - 1];
    var tempValue2;
    for (var i = arr.length - 2; i >= 0; i--){
        tempValue2 = arr[i];
        arr[i] = tempValue1
        tempValue1 = tempValue2;
    }
    arr.pop()
    return tempValue2;
}

A = [1, 2, 3, 4, 5]
console.log(popAtFront(A));
console.log(popAtFront(A));
console.log(popAtFront(A));
console.log(popAtFront(A));
console.log(popAtFront(A));