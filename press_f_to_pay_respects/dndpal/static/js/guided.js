var chrID;
var proflist = new Array(18);
var pageProf = $('#Skills-body').find("input");
function getProflist() {
    for(p=0 ; p<18 ; p++){
      proflist[p] = pageProf[p].checked;
    }
    return proflist.toString();
}



function setProflist(profstr) {
  proflist = profstr.split(",");
  console.log(proflist);

    for(qwopa=0 ; qwopa<18 ; qwopa++){
      pageProf[qwopa].checked = (proflist[qwopa] == 'true'); ;
    }
}





$('#save').click(function(){
  chrID = window.location.href.split('/');
  chrID = chrID[chrID.length - 1];
  var sendspells = JSON.stringify(knownSpellList);
  var json_save ={
    id: chrID,
    lvl:lvl.value,
    exp:$('#exp-field').val(),
    skills: getProflist() ,
    MaxHp: HitPoints.value,
    TempHp : $('#TempHit').val() ,
    CurrentHp:$('#Currenthp').val(),
    Ac:$('#AC').val(),
    Inititive: $('#Init').val(),
    Speed:$('#Speed').val(),
    str: $('#str').val(),
    dex: $('#dex').val(),
    con: $('#con').val(),
    int: $('#int').val(),
    wis: $('#wis').val(),
    chr: $('#chr').val(),
    spells: sendspells ,
    spellslots: pageSlots.toString(),
    Copper:$('#Copper').val(),
    Silver:$('#Silver').val(),
    Gold:$('#Gold').val()
  };
  if(json_save.spells === []){
    json_save.spells = 'none';

  }

  chrID = chrID[chrID.length - 1];
  $.ajax({
      url: "/dndpal/ajax/test_post/",
      type: "POST",
      contentType: 'application/json',
      dataType:'json',
      data:JSON.stringify(json_save),
      success: function (data) {
        alert('saved');
      }
    });

});
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});






var Proficiency = document.getElementById('Proficiency');
document.getElementById('Proficiency').onchange = function(){thing()};
function thing(){
  updatestr();
  updatedex();
  updatecon();
  updatewis();
  updateint();
  updatechr();


}
// on load functiuon handling loading or initial setup
$( window ).on( "load", function() {
  chrID = window.location.href.split('/');
  chrID = chrID[chrID.length - 1];
  control = parseInt(lvl.value);
  thing();

  if(control == 0)
  setTimeout(function(){leveling()},200);
  else{
    $.ajax({
        url: "/dndpal/ajax/get_character/" + chrID + "/",
        success: function (data) {


          var loadtuffthings = JSON.parse(data);
          // get all abilities
          loadAblilities();

          // set proficiencies
          setProflist(loadtuffthings[0].fields.proficiency_list);
          thing();
          // load spells
          var loadspells = loadtuffthings[0].fields.spell_list;
          loadspells = JSON.parse(loadspells);
          for(spl in loadspells){
            appendmodalspell(0, pageSpelllvls[(loadspells[spl].spell_level - 1)] , loadspells[spl].name , false, 0);
          }
          knownSpellList = loadspells;
          // load spell slots
          var temppageSlots = (loadtuffthings[0].fields.ability_list).split(",");
          for(qwop = 1 ; qwop < temppageSlots.length ; qwop++){
            apendSlots("Slot"+ qwop,temppageSlots[qwop]);
          }
        }
      });

  }

});

function loadAblilities() {
  $.ajax({
      url: "/dndpal/ajax/get_abilites/" + cname.value + "/"+ lvl.value + "/",
      success: function (datas) {
        var loadab = JSON.parse(datas);
        for(pap in loadab){
          AddAbility(loadab[pap].fields.description ,loadab[pap].fields.name);
        }

      }
    });

}

/*Ability Scores*/
  /* changes everything related to strength*/
  document.getElementById("str").onchange = function() {updatestr()};
    var str = document.getElementById("str");
    var strmd = document.getElementById("strmd");
    var strmod = str.value;
    function updatestr(){
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
        var AcroPro = Proficiency.value;
        if(AcroDP.checked){
          AcroPro = AcroPro *2;
        }
        if(Acrop.checked){
          Acro.value = '+'+(+AcroPro + +dexmod);
        }else{
          Acro.value = dexmd.value;
        }
      }

    /*cahnges the Animal Handling skill on click*/
    document.getElementById("AnimP").onclick = function() {updateAnim()};
      var Anim = document.getElementById('Anim');
      var Animp = document.getElementById('AnimP');
      function updateAnim(){
        var AnimPro = Proficiency.value;
        if(AnimDP.checked){
          AnimPro = AnimPro *2;
        }
        if(Animp.checked){
          Anim.value = '+'+(+AnimPro + +wismod);
        }else{
          Anim.value = wismd.value;
        }
    }

    /*cahnges the Arcana skill on click*/
    document.getElementById("ArcaP").onclick = function() {updateArca()};
      var Arca = document.getElementById('Arca');
      var Arcap = document.getElementById('ArcaP');
      function updateArca(){
        var ArcaPro = Proficiency.value;
        if(ArcaDP.checked){
          ArcaPro = ArcaPro *2;
        }
        if(Arcap.checked){
          Arca.value = '+'+(+ArcaPro + +intmod);
        }else{
          Arca.value = intmd.value;
        }
    }

    /*cahnges the Athletics skill on click*/
    document.getElementById("AthlP").onclick = function() {updateAthl()};
      var Athl = document.getElementById('Athl');
      var Athlp = document.getElementById('AthlP');
      function updateAthl(){
        var AthlPro = Proficiency.value;
        if(AthlDP.checked){
          AthlPro = AthlPro *2;
        }
        if(Athlp.checked){
          Athl.value = '+'+(+AthlPro + +strmod);
        }else{
          Athl.value = strmd.value;
        }
      }

    /*cahnges the Deception skill on click*/
    document.getElementById("DeceP").onclick = function() {updateDece()};
      var Dece = document.getElementById('Dece');
      var Decep = document.getElementById('DeceP');
      function updateDece(){
        var DecePro = Proficiency.value;
        if(DeceDP.checked){
          DecePro = DecePro *2;
        }
        if(Decep.checked){
          Dece.value = '+'+(+DecePro + +chrmod);
        }else{
          Dece.value = chrmd.value;
        }
      }

    /*cahnges the History skill on click*/
    document.getElementById("HistP").onclick = function() {updateHist()};
      var Hist = document.getElementById('Hist');
      var Histp = document.getElementById('HistP');
      function updateHist(){
        var HistPro = Proficiency.value;
        if(HistDP.checked){
          HistPro = HistPro *2;
        }
        if(Histp.checked){
          Hist.value = '+'+(+HistPro + +intmod);
        }else{
          Hist.value = intmd.value;
        }
    }

    /*cahnges the Insight skill on click*/
    document.getElementById("InsiP").onclick = function() {updateInsi()};
      var Insi = document.getElementById('Insi');
      var Insip = document.getElementById('InsiP');
      function updateInsi(){
        var InsiPro = Proficiency.value;
        if(InsiDP.checked){
          InsiPro = InsiPro *2;
        }
        if(Insip.checked){
          Insi.value = '+'+(+InsiPro + +wismod);
        }else{
          Insi.value = wismd.value;
        }
      }

    /*cahnges the Intimidation skill on click*/
    document.getElementById("IntiP").onclick = function() {updateInti()};
      var Inti = document.getElementById('Inti');
      var Intip = document.getElementById('IntiP');
      function updateInti(){
        var IntiPro = Proficiency.value;
        if(IntiDP.checked){
          IntiPro = IntiPro *2;
        }
        if(Intip.checked){
          Inti.value = '+'+(+IntiPro + +chrmod);
        }else{
          Inti.value = chrmd.value;
        }
      }

    /*cahnges the Investigation skill on click*/
    document.getElementById("InveP").onclick = function() {updateInve()};
      var Inve = document.getElementById('Inve');
      var Invep = document.getElementById('InveP');
      function updateInve(){
        var InvePro = Proficiency.value;
        if(InveDP.checked){
          InvePro = InvePro *2;
        }
        if(Invep.checked){
          Inve.value = '+'+(+InvePro + +intmod);
        }else{
          Inve.value = intmd.value;
        }
    }

    /*cahnges the Medicine skill on click*/
    document.getElementById("MediP").onclick = function() {updateMedi()};
      var Medi = document.getElementById('Medi');
      var Medip = document.getElementById('MediP');
      function updateMedi(){
        var MediPro = Proficiency.value;
        if(MediDP.checked){
          MediPro = MediPro *2;
        }
        if(Medip.checked){
          Medi.value = '+'+(+MediPro + +wismod);
        }else{
          Medi.value = wismd.value;
        }
    }

    /*cahnges the Nature skill on click*/
    document.getElementById("NatuP").onclick = function() {updateNatu()};
      var Natu = document.getElementById('Natu');
      var Natup = document.getElementById('NatuP');
      function updateNatu(){
        var NatuPro = Proficiency.value;
        if(NatuDP.checked){
          NatuPro = NatuPro *2;
        }
        if(Natup.checked){
          Natu.value = '+'+(+NatuPro + +intmod);
        }else{
          Natu.value = intmd.value;
        }
      }

    /*cahnges the Perseption skill on click*/
    document.getElementById("PercP").onclick = function() {updatePerc()};
      var Perc = document.getElementById('Perc');
      var Percp = document.getElementById('PercP');
      function updatePerc(){
        var PercPro = Proficiency.value;
        if(PercDP.checked){
          PercPro = PercPro *2;
        }
        if(Percp.checked){
          Perc.value = '+'+(+PercPro + +wismod);
      }else{
        Perc.value = wismd.value;
        }
      }

    /*cahnges the performance skill on click*/
    document.getElementById("PerfP").onclick = function() {updatePerf()};
      var Perf = document.getElementById('Perf');
      var Perfp = document.getElementById('PerfP');
      function updatePerf(){
        var PerfPro = Proficiency.value;
        if(PerfDP.checked){
          PerfPro = PerfPro *2;
        }
        if(Perfp.checked){
          Perf.value = '+'+(+PerfPro + +chrmod);
        }else{
          Perf.value = chrmd.value;
        }
      }

    /*cahnges the Persuation skill on click*/
    document.getElementById("PersP").onclick = function() {updatePers()};
      var Pers = document.getElementById('Pers');
      var Persp = document.getElementById('PersP');
        function updatePers(){
          var PersPro = Proficiency.value;
          if(PersDP.checked){
            PersPro = PersPro *2;
          }
          if(Persp.checked){
            Pers.value = '+'+(+PersPro + +chrmod);
          }else{
            Pers.value = chrmd.value;
          }
      }

    /*cahnges the Religion skill on click*/
    document.getElementById("ReliP").onclick = function() {updateReli()};
      var Reli = document.getElementById('Reli');
      var Relip = document.getElementById('ReliP');
      function updateReli(){
        var ReliPro = Proficiency.value;
        if(ReliDP.checked){
          ReliPro = ReliPro *2;
        }
        if(Relip.checked){
          Reli.value = '+'+(+ReliPro + +intmod);
        }else{
          Reli.value = intmd.value;
        }
      }

    /*cahnges the Sleight of Hands skill on click*/
    document.getElementById("SleiP").onclick = function() {updateSlei()};
      var Slei = document.getElementById('Slei');
      var Sleip = document.getElementById('SleiP');
        function updateSlei(){
          var SleiPro = Proficiency.value;
          if(SleiDP.checked){
            SleiPro = SleiPro *2;
          }
          if(Sleip.checked){
            Slei.value = '+'+(+SleiPro + +dexmod);
          }else{
            Slei.value = dexmd.value;
          }
      }

    /*cahnges the Stealth skill on click*/
    document.getElementById("SteaP").onclick = function() {updateStea()};
      var Stea = document.getElementById('Stea');
      var Steap = document.getElementById('SteaP');
      function updateStea(){
        var SteaPro = Proficiency.value;
        if(SteaDP.checked){
          SteaPro = SteaPro *2;
        }
        if(Steap.checked){
          Stea.value = '+'+(+SteaPro + +dexmod);
        }else{
          Stea.value = dexmd.value;
        }
      }

      /*cahnges the Survival skill on click*/
      document.getElementById("SurvP").onclick = function() {updateSurv()};
        var Surv = document.getElementById('Surv');
        var Survp = document.getElementById('SurvP');
        function updateSurv(){
          var SurvPro = Proficiency.value;
          if(SurvDP.checked){
            SurvPro = SurvPro *2;
          }
          if(Survp.checked){
          Surv.value = '+'+(+SurvPro + +wismod);
          }else{
            Surv.value = wismd.value;
          }
        }


    /*double proficency modal things*/

    // Get the modal
var Dpmodal = document.getElementById('double-pro-modal');

// Get the button that opens the modal
var Dpbtn = document.getElementById("DP-btn");
Dpbtn.onclick = function(){
  Dpmodal.style.display = "";
}

// When the user clicks the button, open the modal
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

  function getValues(url) {
      var result = null;
      $.ajax({
          url: url,
          type: 'get',
          async: false,
          success: function(data) {
              result = data;
          }
      });
     return result;
  }

 //level up shit

    //grabing stuff needed
      var pageSlots = [0,0,0,0,0,0,0,0,0,0];
      var levelshit = null;
      var control;
      var moreControl;
      var lvlbtn = document.getElementById('level-up-btn');
      var lvl = document.getElementById('level-field');
      lvlbtn.onclick = function(){
        control = parseInt(lvl.value);
        leveling();
      }

        //main controll function
        function leveling(){
          if(parseInt(lvl.value) === 0 && control < 3)
          prestuff();
          else{

            if(levelshit == null){
              lvl.value = parseInt(lvl.value) + 1;
              moreControl = 0;
              levelshit = getValues('/dndpal/ajax/get_features/'+ cname.value + '/'+ lvl.value);
              levelshit = JSON.parse(levelshit);
              levelshit.push( JSON.parse('{"fields":{"feature_type":"Health"}}') );
              levelshit.push( JSON.parse('{"fields":{"feature_type":"end"}}') );
              leveling();
            }else{
                var currentAbility = levelshit[moreControl].fields.feature_type;


                  switch (currentAbility){
                    case 'Ability':
                      AddAbility(levelshit[moreControl].fields.description,levelshit[moreControl].fields.name)
                      moreControl = moreControl + 1;
                      leveling();
                      break;
                    case 'end':
                      levelshit = null;
                      break;
                    case 'Spell Slots':
                    var doing =  JSON.parse(levelshit[moreControl].fields.description);

                    for (var key in doing) {
                        if(key == "Slot0"){}
                        else
                          apendSlots(key,doing[key]);
                      }
                        moreControl = moreControl + 1;
                      leveling();
                    break;

                    case 'New Spells':
                      var newSpells = parseInt(levelshit[moreControl].fields.description);

                      $.ajax({
                          url: "/dndpal/ajax/get_spells/"+ cname.value + "/"+lvl.value + "/",
                          success: function (data) {
                            for(var sp in data){
                              var cursp = data[sp];
                              spellarray.push(cursp);
                              if(! spellExists(cursp.name)){
                                appendmodalspell(cursp.ranking , modalSpelllvls[(cursp.spell_level - 1)] , cursp.name , true , sp);
                              }
                            }
                            $('#Spell-modal').show();
                          }
                        });
                      moreControl = moreControl + 1;
                      break;
                      case 'Health':
                        Healthmain();
                        moreControl = moreControl + 1;
                        break;
                    default:

                    moreControl = moreControl + 1;
                    leveling();
                  }//end switch
            }
          }// end if level is zero controll loop
        }// end leveling

        function prestuff() {
          switch (control) {
            case 0:
              statsMain();
              break;
            case 1:
              Skillsmain();
              break;
            case 2:
              control = control + 1;
              leveling();
              break;
          }
          control = control + 1;
        }//end prestuff





// Health modal stuff
  // grabing
  var Healthmodal = document.getElementById('Health-modal');

  var Roll = document.getElementById('Roll');
  var Rollval = document.getElementById('Roll-value');
  var Rollbtn = document.getElementById('Roll-btn');

  var Average = document.getElementById('Average');
  var Averageval = document.getElementById('Average-value');
  var Averagebtn = document.getElementById('Average-btn');

  var Random = document.getElementById('Random');
  var Randomval = document.getElementById('Random-value');
  var Randombtn = document.getElementById('Random-btn');

  var HitPoints = document.getElementById('HitPoints');
  var Hitdie;
  var cname = document.getElementById('class-field');
 // Health "main"
  function Healthmain(){
    //ajax call to set hit die
    var healthstr = '/dndpal/ajax/get_health/'+ cname.value;
    $.ajax({
        url: healthstr,
        success: function (data) {
          if(lvl.value == 1){
            addHealth(data.Hitdie);
          }else{
          setHitdie(data.Hitdie);
          }
        }
      });
  }

  function setHitdie(gg){
    Healthmodal.style.display = "Block";
    Hitdie = gg;
    Roll.innerHTML = 'Roll a d' + Hitdie;
    Averageval.value = Math.floor(Hitdie/2) + 1;
  }

  Rollbtn.onclick = function(){
    if(Rollval.value <= Hitdie){
    addHealth(Rollval.value);
    }
  }

  Averagebtn.onclick = function(){addHealth(Averageval.value);}

  Randombtn.onclick = function(){
    addHealth(Math.floor(Math.random() * Hitdie));
  }

  function addHealth(healthval){
    HitPoints.value =parseInt(HitPoints.value) + parseInt(healthval) +(parseInt(conmd.value.replace('+','')));

    $('#Currenthp').val(parseInt($('#Currenthp').val()) + parseInt(healthval) +(parseInt(conmd.value.replace('+',''))));
    Healthmodal.style.display = "";
    leveling();
  }
// end Health

// class skills

function Skillsmain() {
  $('#Skills-modal').show();
  $("#Skills-modal").find('input:checkbox').each(function(e){
    $(this).prop('disabled', true);
  });
  $.ajax({
      url: '/dndpal/ajax/get_skills/'+ cname.value,
      success: function (data) {
        var d = data.skills.split(',');
        enableshit(d);
      }
    });
}
function enableshit(skillarray) {
  skillarray.forEach( function(item,index,array){
      var sub = item.substring(0,4);
      sub = sub + 'P';
      document.getElementById(sub).disabled = false;
  });
}
$('#skill-kill').click(function(){
  $('#Skills-modal').hide();
  leveling();
});

// end skills

// stats
function statsMain() {
$('#Stat-modal').show();
}

$('#Stats-kill').click(
  function(){
      $("#str").val($("#Temp-str").val()) ;
      $("#dex").val($("#Temp-dex").val()) ;
      $("#con").val($("#Temp-con").val()) ;
      $("#int").val($("#Temp-int").val()) ;
      $("#wis").val($("#Temp-wis").val()) ;
      $("#chr").val($("#Temp-chr").val()) ;
      updatestr();
      updatedex();
      updatecon();
      updateint();
      updatewis();
      updatechr();
      $('#Stat-modal').hide();
      leveling();
  });

// adding abilites to the view
  function AddAbility(description , name) {
    $('#Ability-list').append(
      `
      <li>
        <div class="card">
          <h6  class="card-header">  ${name}   </h6>
          <p class="card-body"> ${description}   </p>
        </div>
      </li>
      `
    );

  }
// spells and spell shit
  // adding spell slots
  function apendSlots(slotname,slotamount) {
    var slotnum = slotname;
    slotnum = slotnum.replace("Slot","");
    slotnum = parseInt(slotnum);
    var slotcount = parseInt(slotamount)
    if(slotcount > pageSlots[slotnum]){
      for(slotcount ; slotcount > pageSlots[slotnum];slotcount--)
        $("#"+slotname).append(
          `
          <li>
            <form class="form-inline">
              <div class="form-group">
                <input type="text" class="form-control">
              </div>
              <div class="form-check">
                <input class="form-check-input position-static" type="checkbox" value="option1" aria-label="...">
              </div>
            </form>
          </li>
          `
        );
      pageSlots[slotnum] = parseInt(slotamount);
    }
  }
// closing spell modal
$('#Close-spells').click(function(){

  $('#Spell-modal-body').find("li").each(function(){
    var toAdd = $(this).find("div")[0];

    if(toAdd.classList.contains("selected")){
      var toAddId = toAdd.id;
      toAddId = spellarray[toAddId];
      appendmodalspell(0, pageSpelllvls[(toAddId.spell_level - 1)] , toAddId.name , false, 0);
      knownSpellList.push(toAddId);
    }
    $(this).remove();
  });
  spellarray = [];
    $('#Spell-modal').hide();
    leveling();
});
// cheak if spell is already on page
function spellExists(splname) {
  for(i =0; i < knownSpellList.length; i++){
    if(splname == knownSpellList[i].name)
      return true;

  }
  return false;
}

//spell on click selection
function Selectedthing(e){

  var elem = $(e).clone().wrap('<li>').html();
  var po = $(e);
  po = po[0].parentElement.parentElement;
  if( po.classList.contains('selected') ){
    po.classList.remove('selected');
  }else{
    po.classList.add('selected');
  }

}
// FILLING OUT  spell modal
  // get all the modal spell positions
  var modalSpelllvls = $('#Spell-modal-body').find("p");
  var pageSpelllvls = $('#spell-list-body').find("p");
  var spellarray = []; // temp spell list for appending spells to the spell list on page
  var knownSpellList = []; // list of known spells ie spells appended to the spell list on page
  // add shit to the modal
  function appendmodalspell(ranking , place, spell, clickable , pos) {
    var rank;
    switch (ranking) {
      case 0:
        rank = "zero";
        break;
      case 1:
        rank = "one";
        break;
      case 2:
        rank = "two";
        break;
      case 3:
        rank = "three";
        break;
      case 4:
        rank = "four";
        break;
      case 5:
        rank = "five";
        break;
      default:
    }
    var cl = '';
    if(clickable){
      cl = 'onclick="Selectedthing(this)"'
    }

    $(place).after(
      `
      <li>
        <div class="card ${rank}" id = "${pos}">
            <div class="row" >
              <div class="col" ${cl}>
                <h6 class="card-header col">${spell}</h6>
              </div>
              <div class="col-4">
               <a href="http://127.0.0.1:8000/dndpal/spell/${spell}" target="_blank" class="btn btn-primary col">More Info</a>
              </div>
            </div>
        </div>
      </li>
      `
    );
  }
