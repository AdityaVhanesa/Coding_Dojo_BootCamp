function arrayWithOdd(range){
    var oddArray = [];
    for ( var i = 0; i <= range; i++){
        if ( i % 2 != 0){
            oddArray.push(i);
        }
    }
    return oddArray;
}

console.log(arrayWithOdd(255));