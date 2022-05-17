// Rotate given array


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


A = [1,2,3,4,5,6,7,8,9,10,11];
rotateArr(A, -3);
console.log(A);