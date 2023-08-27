
// Every minute plays a short gif "video" of a Rubik's Cube doing a sequence of twists
// There are numbers on the cube so every minute a new number is shifted into place
// to represent the time of day

Number.prototype.pad2 = function() {
  var s = String(this);
  while (s.length < (2)) {s = "0" + s;}
  return s;
}

//Gets calendar & clock text display
function rubiksClock() {

  const date = new Date(); //gets your local date & time
  const time = date.toLocaleTimeString([], {hour: '2-digit', minute:'2-digit'}); //a time string value

  const hours = (date.getHours()).pad2()
  const minutes = (date.getMinutes()).pad2()

  var cube = new Image();
  var cubeElement = document.getElementById("cube"); // assumes an element with id "banner" contains the banner image - you can get the element however you want.
  
  var hires = false
  var clockType = "12" // "24"

  if (hires) {
    cube.src = "videos/" + clockType + "hourclock-800x480-gif/rubiks-clock-"+hours+minutes+".gif";
  } else {
    cube.src = "videos/" + clockType + "hourclock-200x120/rubiks-clock-"+hours+minutes+".gif";
  }
  cube.onload = function() {
  cubeElement.removeChild(cubeElement.lastChild);
  cubeElement.appendChild(cube);
  };

}


//runs function after html document loads
window.onload = function() {
  
  rubiksClock(); //runs once without delay

  setInterval(function () { rubiksClock() }, 1000); //keeps time running every second (millisecond)
};
