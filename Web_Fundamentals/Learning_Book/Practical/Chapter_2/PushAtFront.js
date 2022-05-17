//Given an array and an additional value, insert this
// value at the beginning of the array. Do this
// without using any built-in array methods.

function pushAtFront(arr, value){
    if (arr.length == 0){
        arr[0] = value;
        return
    }
    var tempValue1 = arr[0];
    var tempValue2;
    arr[0] = value
    for (var i = 1; i < arr.length; i++){
        tempValue2 = arr[i];
        arr[i] = tempValue1;
        tempValue1 = tempValue2;
    }
    arr[arr.length] = tempValue1;
}
A = [];
pushAtFront(A, 0);
pushAtFront(A, -1);
console.log(A);