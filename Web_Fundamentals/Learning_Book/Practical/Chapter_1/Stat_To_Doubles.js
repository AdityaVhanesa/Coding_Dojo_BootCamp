// Implement a ‘die’ that randomly returns an
// integer between 1 and 6 inclusive. Roll a pair of
// these dice, tracking the statistics until doubles
// are rolled. Display the number of rolls, min, max,
// and average.

function die(){
    return Math.floor(Math.random() * 7);
}

function rollDie(){
    var Die_Result = [1,  2]
    var dieRolled = 0;
    var max = Number.NEGATIVE_INFINITY;
    var min = Number.POSITIVE_INFINITY;
    var sum = 0
    var numberOfDiesRolled = 2
    while (Die_Result[0] != Die_Result[1]){
        Die_Result = [die(), die()];
        dieRolled ++;
        sum = Die_Result[0] + Die_Result[1];
        for (var i = 0; i < numberOfDiesRolled; i++){
            var value = Die_Result[i];
            if (value > max){
                max = value;
            }

            if (value < min){
                min = value;
            }
        }
        console.log("Number of roll --> " + dieRolled + " | Average --> " + (sum/ numberOfDiesRolled) + " | Min --> " + min + " | Max --> " + max);
        sum = 0;
    }
}

rollDie();