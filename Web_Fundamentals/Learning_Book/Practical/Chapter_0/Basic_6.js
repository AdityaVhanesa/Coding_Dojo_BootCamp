function minMaxAverage(arr){
    var maximumValue = Number.NEGATIVE_INFINITY;
    var miniMumValue = Number.POSITIVE_INFINITY;
    var sum = 0;

    for (var i = 0; i < arr.length; i++){
        var value = arr[i];
        if (value < miniMumValue){
            miniMumValue = value;
        } 
        if (value > maximumValue){
            maximumValue = value;
        }
        sum += value
    }

    return [miniMumValue, maximumValue, sum / arr.length];
}

var result = minMaxAverage([1,2,3,4,5]);
console.log(result);