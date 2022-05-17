// This is Fizz Buzz challange.
var loopSize = 100;
for (var i = 1; i <= loopSize; i++){
    if ((i % 3 == 0) && (i % 5 != 0)) {
        console.log("Fizz");
    }else if((i % 5 == 0) && (i % 3 != 0)){
        console.log("Buzz");
    } else if (i % 15 == 0){
        console.log("FizzBuzz");
    } else {
        console.log(i);
    }
}