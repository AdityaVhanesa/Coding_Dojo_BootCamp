// implement fibonachi number 

function fibonacci(index){
    var first_number = 0;
    var second_number = 1;
    if (index == 0){
        return first_number;
    } else if (index == 1){
        return second_number;
    }
    var new_number = 0;
    for (var i = 1; i < index; i++){
        new_number = first_number + second_number;
        first_number = second_number;
        second_number = new_number;
    }
    return new_number;
}

console.log(fibonacci(50))