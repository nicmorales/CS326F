
/* changes everything related to strength*/
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

/* changes everything related to dex*/
document.getElementById("dex").onchange = function() {updatedex()};

function updatedex(){
  var x = document.getElementById("dex");
  var y = document.getElementById("dexmd");

  var z = x.value;

  z = Math.floor(z/2);
  z = z-5;
  if(z>-1){
    y.value = '+'+ z;
  }else
    y.value = z;
}

/* changes everything related to con*/
document.getElementById("con").onchange = function() {updatecon()};

function updatecon(){
  var x = document.getElementById("con");
  var y = document.getElementById("conmd");

  var z = x.value;

  z = Math.floor(z/2);
  z = z-5;
  if(z>-1){
    y.value = '+'+ z;
  }else
    y.value = z;
}

/* changes everything related to int*/
document.getElementById("int").onchange = function() {updateint()};

function updateint(){
  var x = document.getElementById("int");
  var y = document.getElementById("intmd");

  var z = x.value;

  z = Math.floor(z/2);
  z = z-5;
  if(z>-1){
    y.value = '+'+ z;
  }else
    y.value = z;
}

/* changes everything related to wis*/
document.getElementById("wis").onchange = function() {updatewis()};

function updatewis(){
  var x = document.getElementById("wis");
  var y = document.getElementById("wismd");

  var z = x.value;

  z = Math.floor(z/2);
  z = z-5;
  if(z>-1){
    y.value = '+'+ z;
  }else
    y.value = z;
}

/* changes everything related to chr*/
document.getElementById("chr").onchange = function() {updatechr()};

function updatechr(){
  var x = document.getElementById("chr");
  var y = document.getElementById("chrmd");

  var z = x.value;

  z = Math.floor(z/2);
  z = z-5;
  if(z>-1){
    y.value = '+'+ z;
  }else
    y.value = z;
}
