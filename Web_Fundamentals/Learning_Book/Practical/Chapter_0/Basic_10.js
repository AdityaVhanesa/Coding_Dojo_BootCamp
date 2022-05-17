// Print Average

function printAverage(arr){
    var sum = 0
    for ( var i = 0; i < arr.length; i++){
        sum += arr[i];
    }
    console.log("Average value is --> " + sum / arr.length);
}

printAverage([1,2,3,4,5]);