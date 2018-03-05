var Proficiency = document.getElementById('Proficiency');
/*Ability Scores*/
  /* changes everything related to strength*/
  document.getElementById("str").onchange = function() {updateStr()};
    var str = document.getElementById("str");
    var strmd = document.getElementById("strmd");
    var strmod = str.value;
    function updateStr(){
      strmod = str.value;
      strmod = Math.floor(strmod/2);
      strmod = strmod-5;
      if(strmod>-1){
        strmd.value = '+'+ strmod;
      }else{
        strmd.value = strmod;
      }
      updateAthl();
    }
  /* changes everything related to dex*/
  document.getElementById("dex").onchange = function() {updatedex()};
    var dex = document.getElementById("dex");
    var dexmd = document.getElementById("dexmd");
    var dexmod = dex.value;
    function updatedex(){
      dexmod = dex.value;
      dexmod = Math.floor(dexmod/2);
      dexmod = dexmod-5;
      if(dexmod>-1){
        dexmd.value = '+'+ dexmod;
      }else
        dexmd.value = dexmod;
    }
  /* changes everything related to con*/
  document.getElementById("con").onchange = function() {updatecon()};
    var con = document.getElementById("con");
    var conmd = document.getElementById("conmd");
    var conmod = con.value;
    function updatecon(){
       conmod = con.value;

      conmod = Math.floor(conmod/2);
      conmod = conmod-5;
      if(conmod>-1){
        conmd.value = '+'+ conmod;
      }else
        conmd.value = conmod;
    }
  /* changes everything related to int*/
  document.getElementById("int").onchange = function() {updateint()};
    var int = document.getElementById("int");
    var intmd = document.getElementById("intmd");
    var intmod = int.value;
    function updateint(){

      intmod = int.value;
      intmod = Math.floor(intmod/2);
      intmod = intmod-5;
      if(intmod>-1){
        intmd.value = '+'+ intmod;
      }else
        intmd.value = intmod;
     }
  /* changes everything related to wis*/
  document.getElementById("wis").onchange = function() {updatewis()};
    var wis = document.getElementById("wis");
    var wismd = document.getElementById("wismd");
    var wismod = wis.value;
    function updatewis(){

      wismod = wis.value;
      wismod = Math.floor(wismod/2);
      wismod = wismod-5;
      if(wismod>-1){
        wismd.value = '+'+ wismod;
      }else
        wismd.value = wismod;
    }
  /* changes everything related to chr*/
  document.getElementById("chr").onchange = function() {updatechr()};
    var chr = document.getElementById("chr");
    var chrmd = document.getElementById("chrmd");
    var chrmod = chr.value;
    function updatechr(){

      chrmod = chr.value;
      chrmod = Math.floor(chrmod/2);
      chrmod = chrmod-5;
      if(chrmod>-1){
        chrmd.value = '+'+ chrmod;
      }else
        chrmd.value = chrmod;
    }

/*Skills*/
  /*cahnges the Acrobatics skill on click*/
  document.getElementById("AcroP").onclick = function() {updateAcro()};
    var Acrobatics = document.getElementById('Acro');
    var Acrobaticsp = document.getElementById('AcroP');
    function updateAcro(){
      if(Acrobaticsp.checked){
      Acrobatics.value = '+'+(parseInt(Proficiency.innerHTML) + dexmod);
      }else{
        Acrobatics.value = dexmd.value;
      }
    }

  /*cahnges the AnimalH skill on click*/
  document.getElementById("AnimP").onclick = function() {updateAnim()};
    var AnimalH = document.getElementById('Anim');
    var AnimalHp = document.getElementById('AnimP');
    function updateAnim(){
      if(AnimalHp.checked){
      AnimalH.value = '+'+(parseInt(Proficiency.innerHTML) + wismod);
      }else{
        AnimalH.value = wismd.value;
      }
    }

  /*cahnges the Arcana skill on click*/
  document.getElementById("ArcaP").onclick = function() {updateArca()};
    var Arcana = document.getElementById('Arca');
    var Arcanap = document.getElementById('ArcaP');
    function updateArca(){
      if(Arcanap.checked){
      Arcana.value = '+'+(parseInt(Proficiency.innerHTML) + intmod);
      }else{
        Arcana.value = intmd.value;
      }
    }

  /*cahnges the athlectics skill on click*/
  document.getElementById("AthlP").onclick = function() {updateAthl()};
    var Athletics = document.getElementById('Athl');
    var Athleticsp = document.getElementById('AthlP');
    function updateAthl(){
      if(Athleticsp.checked){
      Athletics.value = '+'+(parseInt(Proficiency.innerHTML) + strmod);
      }else{
        Athletics.value = strmd.value;
      }
    }

  /*cahnges the Deception skill on click*/
  document.getElementById("DeceP").onclick = function() {updateDece()};
    var Deception = document.getElementById('Dece');
    var Deceptionp = document.getElementById('DeceP');
    function updateDece(){
      if(Deceptionp.checked){
      Deception.value = '+'+(parseInt(Proficiency.innerHTML) + chrmod);
      }else{
        Deception.value = chrmd.value;
      }
    }
    
  /*cahnges the History skill on click*/
  document.getElementById("HistP").onclick = function() {updateHist()};
    var Histor = document.getElementById('Hist');
    var Historyp = document.getElementById('HistP');
    function updateHist(){
      if(Historyp.checked){
      Histor.value = '+'+(parseInt(Proficiency.innerHTML) + xxxmod);
      }else{
        Histor.value = xxxmd.value;
      }
    }

  /*cahnges the Insight skill on click*/
  document.getElementById("InsiP").onclick = function() {updateInsi()};
    var Insight = document.getElementById('Insi');
    var Insightp = document.getElementById('InsiP');
    function updateInsi(){
      if(Insightp.checked){
      Insight.value = '+'+(parseInt(Proficiency.innerHTML) + xxxmod);
      }else{
        Insight.value = xxxmd.value;
      }
    }

  /*cahnges the Intimidation skill on click*/
  document.getElementById("IntiP").onclick = function() {updateInti()};
    var Intimidation = document.getElementById('Inti');
    var Intimidationp = document.getElementById('IntiP');
    function updateInti(){
      if(Intimidationp.checked){
      Intimidation.value = '+'+(parseInt(Proficiency.innerHTML) + xxxmod);
      }else{
        Intimidation.value = xxxmd.value;
      }
    }

  /*cahnges the Investigation skill on click*/
  document.getElementById("InveP").onclick = function() {updateInve()};
    var Investigation = document.getElementById('Inve');
    var Investigationp = document.getElementById('InveP');
    function updateInve(){
      if(Investigationp.checked){
      Investigation.value = '+'+(parseInt(Proficiency.innerHTML) + xxxmod);
      }else{
        Investigation.value = xxxmd.value;
      }
    }

  /*cahnges the Medicine skill on click*/
  document.getElementById("MediP").onclick = function() {updateMedi()};
    var Medicine = document.getElementById('Medi');
    var Medicinep = document.getElementById('MediP');
    function updateMedi(){
      if(Medicinep.checked){
      Medicine.value = '+'+(parseInt(Proficiency.innerHTML) + xxxmod);
      }else{
        Medicine.value = xxxmd.value;
      }
    }

  /*cahnges the Nature skill on click*/
  document.getElementById("NatuP").onclick = function() {updateNatu()};
    var Nature = document.getElementById('Natu');
    var Naturep = document.getElementById('NatuP');
    function updateNatu(){
      if(Naturep.checked){
      Nature.value = '+'+(parseInt(Proficiency.innerHTML) + xxxmod);
      }else{
        Nature.value = xxxmd.value;
      }
    }

  /*cahnges the Perseption skill on click*/
  document.getElementById("PercP").onclick = function() {updatePerc()};
    var Perseption = document.getElementById('Perc');
    var Perseptionp = document.getElementById('PercP');
    function updatePerc(){
      if(Perseptionp.checked){
      Perseption.value = '+'+(parseInt(Proficiency.innerHTML) + xxxmod);
      }else{
        Perseption.value = xxxmd.value;
      }
    }

  /*cahnges the Performance skill on click*/
  document.getElementById("PerfP").onclick = function() {updatePerf()};
    var Performanc = document.getElementById('Perf');
    var Performancep = document.getElementById('PerfP');
    function updatePerf(){
      if(Performancep.checked){
      Performanc.value = '+'+(parseInt(Proficiency.innerHTML) + xxxmod);
      }else{
        Performanc.value = xxxmd.value;
      }
    }

    /*cahnges the Persuation skill on click*/
    document.getElementById("PersP").onclick = function() {updatePers()};
      var Persuation = document.getElementById('Pers');
      var Persuationp = document.getElementById('PersP');
      function updatePers(){
        if(Persuationp.checked){
        Persuation.value = '+'+(parseInt(Proficiency.innerHTML) + xxxmod);
        }else{
          Persuation.value = xxxmd.value;
        }
      }

    /*cahnges the Religion skill on click*/
    document.getElementById("ReliP").onclick = function() {updateReli()};
      var Religion = document.getElementById('Reli');
      var Religionp = document.getElementById('ReliP');
      function updateReli(){
        if(Religionp.checked){
        Religion.value = '+'+(parseInt(Proficiency.innerHTML) + xxxmod);
        }else{
          Religion.value = xxxmd.value;
        }
      }

    /*cahnges the Sleight_of_Hand skill on click*/
    document.getElementById("SleiP").onclick = function() {updateSlei()};
      var Sleight_of_Hand = document.getElementById('Slei');
      var Sleight_of_Handp = document.getElementById('SleiP');
      function updateSlei(){
        if(Sleight_of_Handp.checked){
        Sleight_of_Hand.value = '+'+(parseInt(Proficiency.innerHTML) + xxxmod);
        }else{
          Sleight_of_Hand.value = xxxmd.value;
        }
      }

    /*cahnges the Stealth skill on click*/
    document.getElementById("SteaP").onclick = function() {updateStea()};
      var Stealth = document.getElementById('Stea');
      var Stealthp = document.getElementById('SteaP');
      function updateStea(){
        if(Stealthp.checked){
        Stealth.value = '+'+(parseInt(Proficiency.innerHTML) + xxxmod);
        }else{
          Stealth.value = xxxmd.value;
        }
      }

  /*cahnges the Survival skill on click*/
  document.getElementById("SurvP").onclick = function() {updateSurv()};
    var Survival = document.getElementById('Surv');
    var Survivalp = document.getElementById('SurvP');
    function updateSurv(){
      if(Survivalp.checked){
      Survival.value = '+'+(parseInt(Proficiency.innerHTML) + xxxmod);
      }else{
        Survival.value = xxxmd.value;
      }
    }
