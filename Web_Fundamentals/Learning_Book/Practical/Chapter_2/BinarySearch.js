// implement Binary Search.

function binarySearch(arr, value){
    var arrayLength = arr.length;
    var lower = -1;
    var upper = arrayLength;
    while (true){
        mid = Math.floor((upper + lower) / 2);
        if ( lower + 1 == upper){
            return false;
        } 
        if (arr[mid] == value){
            return mid;
        }

        if (value < arr[mid]) {
            upper = mid;
        } else {
            lower = mid;
        }

    }
}

console.log(binarySearch([1,2,3,4,5,6,10, 11, 12,13], 14));