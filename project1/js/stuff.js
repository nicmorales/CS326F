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
      }else{
        dexmd.value = dexmod;
      }
        updateAcro();
        updateSlei();
        updateStea();
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
      }else{
        conmd.value = conmod;
      }

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
      }else{
        intmd.value = intmod;
      }
      updateArca();
      updateHist();
      updateInve();
      updateNatu();
      updateReli();

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
      }else{
        wismd.value = wismod;
      }

      updateInsi();
      updateAnim();
      updateMedi();
      updatePerc();
      updateSurv();
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
      }else{
        chrmd.value = chrmod;
      }
      updateDece();
      updateInti();
      updatePerf();
      updatePers();
    }



/*Skills*/

    /*cahnges the Acrobatics skill on click*/
    document.getElementById("AcroP").onclick = function() {updateAcro()};
      var Acro = document.getElementById('Acro');
      var Acrop = document.getElementById('AcroP');
      function updateAcro(){
        var AcroPro = parseInt(Proficiency.innerHTML);
        if(AcroDP.checked){
          AcroPro = AcroPro *2;
        }
        if(Acrop.checked){
          Acro.value = '+'+(AcroPro + dexmod);
        }else{
          Acro.value = dex.value;
        }
      }

    /*cahnges the Animal Handling skill on click*/
    document.getElementById("AnimP").onclick = function() {updateAnim()};
      var Anim = document.getElementById('Anim');
      var Animp = document.getElementById('AnimP');
      function updateAnim(){
        var AnimPro = parseInt(Proficiency.innerHTML);
        if(AnimDP.checked){
          AnimPro = AnimPro *2;
        }
        if(Animp.checked){
          Anim.value = '+'+(AnimPro + wismod);
        }else{
          Anim.value = wis.value;
        }
    }

    /*cahnges the Arcana skill on click*/
    document.getElementById("ArcaP").onclick = function() {updateArca()};
      var Arca = document.getElementById('Arca');
      var Arcap = document.getElementById('ArcaP');
      function updateArca(){
        var ArcaPro = parseInt(Proficiency.innerHTML);
        if(ArcaDP.checked){
          ArcaPro = ArcaPro *2;
        }
        if(Arcap.checked){
          Arca.value = '+'+(ArcaPro + intmod);
        }else{
          Arca.value = int.value;
        }
    }

    /*cahnges the Athletics skill on click*/
    document.getElementById("AthlP").onclick = function() {updateAthl()};
      var Athl = document.getElementById('Athl');
      var Athlp = document.getElementById('AthlP');
      function updateAthl(){
        var AthlPro = parseInt(Proficiency.innerHTML);
        if(AthlDP.checked){
          AthlPro = AthlPro *2;
        }
        if(Athlp.checked){
          Athl.value = '+'+(AthlPro + strmod);
        }else{
          Athl.value = str.value;
        }
      }

    /*cahnges the Deception skill on click*/
    document.getElementById("DeceP").onclick = function() {updateDece()};
      var Dece = document.getElementById('Dece');
      var Decep = document.getElementById('DeceP');
      function updateDece(){
        var DecePro = parseInt(Proficiency.innerHTML);
        if(DeceDP.checked){
          DecePro = DecePro *2;
        }
        if(Decep.checked){
          Dece.value = '+'+(DecePro + chrmod);
        }else{
          Dece.value = chr.value;
        }
      }

    /*cahnges the History skill on click*/
    document.getElementById("HistP").onclick = function() {updateHist()};
      var Hist = document.getElementById('Hist');
      var Histp = document.getElementById('HistP');
      function updateHist(){
        var HistPro = parseInt(Proficiency.innerHTML);
        if(HistDP.checked){
          HistPro = HistPro *2;
        }
        if(Histp.checked){
          Hist.value = '+'+(HistPro + intmod);
        }else{
          Hist.value = int.value;
        }
    }

    /*cahnges the Insight skill on click*/
    document.getElementById("InsiP").onclick = function() {updateInsi()};
      var Insi = document.getElementById('Insi');
      var Insip = document.getElementById('InsiP');
      function updateInsi(){
        var InsiPro = parseInt(Proficiency.innerHTML);
        if(InsiDP.checked){
          InsiPro = InsiPro *2;
        }
        if(Insip.checked){
          Insi.value = '+'+(InsiPro + wismod);
        }else{
          Insi.value = wis.value;
        }
      }

    /*cahnges the Intimidation skill on click*/
    document.getElementById("IntiP").onclick = function() {updateInti()};
      var Inti = document.getElementById('Inti');
      var Intip = document.getElementById('IntiP');
      function updateInti(){
        var IntiPro = parseInt(Proficiency.innerHTML);
        if(IntiDP.checked){
          IntiPro = IntiPro *2;
        }
        if(Intip.checked){
          Inti.value = '+'+(IntiPro + chrmod);
        }else{
          Inti.value = chr.value;
        }
      }

    /*cahnges the Investigation skill on click*/
    document.getElementById("InveP").onclick = function() {updateInve()};
      var Inve = document.getElementById('Inve');
      var Invep = document.getElementById('InveP');
      function updateInve(){
        var InvePro = parseInt(Proficiency.innerHTML);
        if(InveDP.checked){
          InvePro = InvePro *2;
        }
        if(Invep.checked){
          Inve.value = '+'+(InvePro + intmod);
        }else{
          Inve.value = int.value;
        }
    }

    /*cahnges the Medicine skill on click*/
    document.getElementById("MediP").onclick = function() {updateMedi()};
      var Medi = document.getElementById('Medi');
      var Medip = document.getElementById('MediP');
      function updateMedi(){
        var MediPro = parseInt(Proficiency.innerHTML);
        if(MediDP.checked){
          MediPro = MediPro *2;
        }
        if(Medip.checked){
          Medi.value = '+'+(MediPro + wismod);
        }else{
          Medi.value = wis.value;
        }
    }

    /*cahnges the Nature skill on click*/
    document.getElementById("NatuP").onclick = function() {updateNatu()};
      var Natu = document.getElementById('Natu');
      var Natup = document.getElementById('NatuP');
      function updateNatu(){
        var NatuPro = parseInt(Proficiency.innerHTML);
        if(NatuDP.checked){
          NatuPro = NatuPro *2;
        }
        if(Natup.checked){
          Natu.value = '+'+(NatuPro + intmod);
        }else{
          Natu.value = int.value;
        }
      }

    /*cahnges the Perseption skill on click*/
    document.getElementById("PercP").onclick = function() {updatePerc()};
      var Perc = document.getElementById('Perc');
      var Percp = document.getElementById('PercP');
      function updatePerc(){
        var PercPro = parseInt(Proficiency.innerHTML);
        if(PercDP.checked){
          PercPro = PercPro *2;
        }
        if(Percp.checked){
          Perc.value = '+'+(PercPro + wismod);
      }else{
        Perc.value = wis.value;
        }
      }

    /*cahnges the performance skill on click*/
    document.getElementById("PerfP").onclick = function() {updatePerf()};
      var Perf = document.getElementById('Perf');
      var Perfp = document.getElementById('PerfP');
      function updatePerf(){
        var PerfPro = parseInt(Proficiency.innerHTML);
        if(PerfDP.checked){
          PerfPro = PerfPro *2;
        }
        if(Perfp.checked){
          Perf.value = '+'+(PerfPro + chrmod);
        }else{
          Perf.value = chr.value;
        }
      }

    /*cahnges the Persuation skill on click*/
    document.getElementById("PersP").onclick = function() {updatePers()};
      var Pers = document.getElementById('Pers');
      var Persp = document.getElementById('PersP');
        function updatePers(){
          var PersPro = parseInt(Proficiency.innerHTML);
          if(PersDP.checked){
            PersPro = PersPro *2;
          }
          if(Persp.checked){
            Pers.value = '+'+(PersPro + chrmod);
          }else{
            Pers.value = chr.value;
          }
      }

    /*cahnges the Religion skill on click*/
    document.getElementById("ReliP").onclick = function() {updateReli()};
      var Reli = document.getElementById('Reli');
      var Relip = document.getElementById('ReliP');
      function updateReli(){
        var ReliPro = parseInt(Proficiency.innerHTML);
        if(ReliDP.checked){
          ReliPro = ReliPro *2;
        }
        if(Relip.checked){
          Reli.value = '+'+(ReliPro + intmod);
        }else{
          Reli.value = int.value;
        }
      }

    /*cahnges the Sleight of Hands skill on click*/
    document.getElementById("SleiP").onclick = function() {updateSlei()};
      var Slei = document.getElementById('Slei');
      var Sleip = document.getElementById('SleiP');
        function updateSlei(){
          var SleiPro = parseInt(Proficiency.innerHTML);
          if(SleiDP.checked){
            SleiPro = SleiPro *2;
          }
          if(Sleip.checked){
            Slei.value = '+'+(SleiPro + dexmod);
          }else{
            Slei.value = dex.value;
          }
      }

    /*cahnges the Stealth skill on click*/
    document.getElementById("SteaP").onclick = function() {updateStea()};
      var Stea = document.getElementById('Stea');
      var Steap = document.getElementById('SteaP');
      function updateStea(){
        var SteaPro = parseInt(Proficiency.innerHTML);
        if(SteaDP.checked){
          SteaPro = SteaPro *2;
        }
        if(Steap.checked){
          Stea.value = '+'+(SteaPro + dexmod);
        }else{
          Stea.value = dex.value;
        }
      }

      /*cahnges the Survival skill on click*/
      document.getElementById("SurvP").onclick = function() {updateSurv()};
        var Surv = document.getElementById('Surv');
        var Survp = document.getElementById('SurvP');
        function updateSurv(){
          var SurvPro = parseInt(Proficiency.innerHTML);
          if(SurvDP.checked){
            SurvPro = SurvPro *2;
          }
          if(Survp.checked){
          Surv.value = '+'+(SurvPro + wismod);
          }else{
            Surv.value = wis.value;
          }
        }


    /*double proficency modal things*/

    // Get the modal
var modal = document.getElementById('myModal');

// Get the button that opens the modal
var btn = document.getElementById("myBtn");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks the button, open the modal
btn.onclick = function() {
    modal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
    modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}

/*sets the skills to use double proficency*/

document.getElementById("AcroDP").onclick = function() {updateAcro()};
var AcroDP = document.getElementById('AcroDP');

document.getElementById("AnimDP").onclick = function() {updateAnim()};
var AnimDP = document.getElementById('AnimDP');

document.getElementById("ArcaDP").onclick = function() {updateArca()};
var ArcaDP = document.getElementById('ArcaDP');

document.getElementById("AthlDP").onclick = function() {updateAthl()};
var AthlDP = document.getElementById('AthlDP');

document.getElementById("DeceDP").onclick = function() {updateDece()};
var DeceDP = document.getElementById('DeceDP');

document.getElementById("HistDP").onclick = function() {updateHist()};
var HistDP = document.getElementById('HistDP');

document.getElementById("InsiDP").onclick = function() {updateInsi()};
var InsiDP = document.getElementById('InsiDP');

document.getElementById("IntiDP").onclick = function() {updateInti()};
var IntiDP = document.getElementById('IntiDP');

document.getElementById("InveDP").onclick = function() {updateInve()};
var InveDP = document.getElementById('InveDP');

document.getElementById("MediDP").onclick = function() {updateMedi()};
var MediDP = document.getElementById('MediDP');

document.getElementById("NatuDP").onclick = function() {updateNatu()};
var NatuDP = document.getElementById('NatuDP');

document.getElementById("PercDP").onclick = function() {updatePerc()};
var PercDP = document.getElementById('PercDP');

document.getElementById("PerfDP").onclick = function() {updatePerf()};
var PerfDP = document.getElementById('PerfDP');

document.getElementById("PersDP").onclick = function() {updatePers()};
var PersDP = document.getElementById('PersDP');

document.getElementById("ReliDP").onclick = function() {updateReli()};
var ReliDP = document.getElementById('ReliDP');

document.getElementById("SleiDP").onclick = function() {updateSlei()};
var SleiDP = document.getElementById('SleiDP');

document.getElementById("SteaDP").onclick = function() {updateStea()};
var SteaDP = document.getElementById('SteaDP');

document.getElementById("SurvDP").onclick = function() {updateSurv()};
var SurvDP = document.getElementById('SurvDP');


/*other shit mabey*/
