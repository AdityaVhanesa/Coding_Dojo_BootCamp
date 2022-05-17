function skylineHeights(arr){
    var maxHeight = Number.NEGATIVE_INFINITY;
    var observableSkyLine = [];
    for (var i = 0; i < arr.length; i++){
        var value = arr[i];
        if (value > maxHeight){
            observableSkyLine.push(value);
            maxHeight = value;
        }
    }

    return observableSkyLine;
}

console.log(skylineHeights([1,-1,7,3, 2, 4, 8, 10, 2, 5, 11, -5, 60]))