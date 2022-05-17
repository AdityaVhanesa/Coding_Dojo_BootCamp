function removeNegative(arr){
    var temp = [];
    for (var i = 0; i < arr.length; i++){
        if ( arr[i] > 0){
            temp.push(arr[i]);
        }
    }
    return temp;
}
