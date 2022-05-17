// . Function that prints the sum of intigers that are divisiable by three and five.

function threesFive(){
    var sum = 0;
    for ( var i = 100; i <= 4000000; i++){
        if ( ((i % 3 == 0) && (i % 5 != 0)) || ((i % 3 != 0) && (i % 5 == 0))){
            sum += i;
        }
    }
    console.log("Sum is --> " + sum);
}

threesFive();


function betterThreesFive(start, end){
    var sum = 0;
    for ( var i = start; i <= end; i++){
        if ( ((i % 3 == 0) && (i % 5 != 0)) || ((i % 3 != 0) && (i % 5 == 0))){
            sum += i;
        }
    }
    console.log("Sum is --> " + sum);
}
betterThreesFive(100, 4000000);