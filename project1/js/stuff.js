document.getElementById("str").onchange = function() {updateStr()};

function updateStr(){
  var x = document.getElementById("str");
  var y = document.getElementById("strmd");

  var z = x.value;

  z = Math.floor(z/2);
  z = z-5;
  if(z>-1){
    y.value = '+'+ z;
  }else
    y.value = z;
}
