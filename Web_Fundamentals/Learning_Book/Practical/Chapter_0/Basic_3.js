function findMaxNumber(arr){
    var minimumNumber = Number.NEGATIVE_INFINITY;
    for ( var i = 0; i < arr.length; i++){
        if (arr[i] > minimumNumber){
            minimumNumber = arr[i];
        }
    }
    console.log("Maximum Number --> " + minimumNumber);
    return minimumNumber;
}

findMaxNumber([1,10, -40000, 30]);
