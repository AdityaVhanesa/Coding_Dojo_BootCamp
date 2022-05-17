
function rotateArr(arr, shiftBy){
    if (shiftBy > 0){
        for( var i = 0; i < shiftBy; i++){
            var temp = arr.pop();
            arr.unshift(temp);
        }
    } else if (shiftBy < 0){
        for(var i = 0; i > shiftBy; i-- ){
            var temp = arr.shift();
            arr.push(temp);
        }
    }
}

function minOfSortedArray(arr){
    var tempVariable1 = arr[0];
    var tempVariable2 = arr[1];
    while (true){
        rotateArr(arr, -1);
        tempVariable2 = arr[1];
        
        if ( arr[0] < tempVariable1 && arr[0] < tempVariable2){
            return arr[0];
        }
        tempVariable1 = arr[0];
    }
}

A = [
    4,  5,  6, 7, 8,
    9, 10, 11,  2,
    3 ];

console.log(minOfSortedArray(A));
