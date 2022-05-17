// Print odd values. 

function printOddValues(maxNumber){
    for(var i = 1; i <= maxNumber; i++){
        if ( i % 2 != 0 ) {
            console.log(i);
        }
    }
}

printOddValues(10);