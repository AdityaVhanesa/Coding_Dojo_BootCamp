// Implement function that accepts cents and computes how to represent that amount with smallest number
// of coins

function generateCoinChanges(cents){
    var availableCoins = [25, 10, 5, 1];
    var coinRepresentation = {
        25 : 0,
        10 : 0,
        5  : 0,
        1  : 0
    };

    for (var i = 0; i < availableCoins.length; i++){
        var value = availableCoins[i];
        var usedCoins = Math.floor(cents / value);
        cents %= value;
        if (usedCoins){
            coinRepresentation[value] = usedCoins;
        }
    }


    console.log("Number of Quaters    --> " + coinRepresentation[25]);
    console.log("Number of Dimes      --> " + coinRepresentation[10]);
    console.log("Number of Five Cents --> " + coinRepresentation[5]);
    console.log("Number of Cents      --> " + coinRepresentation[1]);

}

generateCoinChanges(405);
