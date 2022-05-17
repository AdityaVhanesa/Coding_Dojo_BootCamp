function clockHandAngles(seconds){
    var hour = 0;
    var minute = 0;
    var second = 0;

    hour = Math.floor(seconds / 3600);
    seconds = seconds % 3600;

    minute =  Math.floor(seconds / 60 );
    seconds = seconds % 60;
    second = seconds;

    console.log(hour);
    console.log(minute);
    console.log(second);
    var hourHandAngle = hour * (360 / 12);
    var minuteHandAngle = minute * (360 / 60);
    var secondHandAngle = second * (360 / 60);
    
    console.log("Hour hand angle --> " + hourHandAngle);
    console.log("Minute hand angle --> " + minuteHandAngle);
    console.log("Second hand angle --> " + secondHandAngle);
    
}
clockHandAngles(5000);