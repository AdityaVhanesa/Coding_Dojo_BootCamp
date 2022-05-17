// Sweep for negative values with Dojo.

function negativeSweepWithDojo(arr){
    for (var i = 0; i < arr.length; i++){
        if (arr[i] < 0){
            arr[i] = "Dojo";
        }
    }
    return arr;
}

console.log(negativeSweepWithDojo([1,2,-3,-5,10,11,12,-17]));