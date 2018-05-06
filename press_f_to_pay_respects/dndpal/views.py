from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import json
from django.core import serializers
import math

from django.http import JsonResponse

from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
from .models import *
from django.db import connection



# Registration Stuff

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('character_create')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Character

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

class CharacterCreate(CreateView):
    model = Character
    fields = ['char_name','char_class','race','subrace']
    template_name = "character_create.html"
    success_url =  reverse_lazy('my-characters')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)



def guided(request):
    """
    View function for guided page of site.
    """
    # Generate data needed for page


    # Render the HTML template guided.html with the data in the context variable
    return render(
        request,
        'guided.html',
    )




def home(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    num_armors=Armor.objects.all().count()

    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'home.html',
        context={'num_armors':num_armors},
    )


def alan(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects

    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'guided.html',
    )


def simple(request):
    """
    View function for simple page of site.
    """
    # Generate data needed for page


    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'simple.html',
    )

@login_required
def profile(request):
    """
    View function for simple page of site.
    """
    # Generate data needed for page


    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'profile.html',
    )

def RaceDetailView2(request):
    race = Race.objects.all()
    raceFeatures = RaceFeatures.objects.all()

    return render(
            request,
            'profile.html',
            context={'race':race,'raceFeatures':raceFeatures}
        )


from django.views import generic
from django.db.models import F


class ArmorListView(generic.ListView):
    model = Armor

class ArmorDetailView(generic.DetailView):
    model = Armor

class CharacterClassListView(generic.ListView):
    model = CharacterClass

class CharacterClassDetailView(generic.DetailView):
    model = CharacterClass

    def get_context_data(self, **kwargs):
        context = super(CharacterClassDetailView, self).get_context_data(**kwargs)
        context['classFeatures'] = CharacterClassFeatures.objects.filter(character_class = context['characterclass'])
        context['clas'] = context['characterclass']
        context['hpAverage'] = math.ceil((context['clas'].hitpoints + 1)/2)
        string = context['clas'].armor_prof
        context['armorProf'] = [x.strip() for x in string.split(',')]
        string = context['clas'].weapon_prof
        context['weaponProf'] = [x.strip() for x in string.split(',')]
        string = context['clas'].saving_throws
        context['savingThrows'] = [x.strip() for x in string.split(',')]
        string = context['clas'].skill_list
        context['skillList'] = [x.strip() for x in string.split(',')]
        context['skillLast'] = context['skillList'][-1]
        context['skillList'] = context['skillList'][:-1]
        print('class = '+str(context['characterclass'].name))
        return context

class EquipmentListView(generic.ListView):
    model = Equipment

class EquipmentDetailView(generic.DetailView):
    model = Equipment

class RaceListView(generic.ListView):
    model = Race

class RaceDetailView(generic.DetailView):
    model = Race



    def get_context_data(self, **kwargs):
        context = super(RaceDetailView, self).get_context_data(**kwargs)

        json_data = context['race'].modifiers
        json_parsed = json.loads(json_data)
        strength = '0'
        dexterity = '0'
        constitution = '0'
        intelligence = '0'
        wisdom = '0'
        charisma = '0'
        if 'str' in json_parsed:
            strength = json_parsed['str']
        if 'dex' in json_parsed:
            dexterity = json_parsed['dex']
        if 'con' in json_parsed:
            constitution = json_parsed['con']
        if 'int' in json_parsed:
            intelligence = json_parsed['int']
        if 'wis' in json_parsed:
            wisdom = json_parsed['wis']
        if 'cha' in json_parsed:
            charisma = json_parsed['cha']

        context['raceStr'] = int(strength)
        context['raceDex'] = int(dexterity)
        context['raceCon'] = int(constitution)
        context['raceInt'] = int(intelligence)
        context['raceWis'] = int(wisdom)
        context['raceCha'] = int(charisma)



        context['raceFeatures'] = RaceFeatures.objects.filter(race = context['race'])

        context['subraces'] = Subrace.objects.filter(parent_race = context['race'])


        context['subrace_mods'] = {}
        context['subraceFeatures'] = {}

        for subrace in context['subraces']:
            sub = {}
            sjson_data = subrace.modifiers
            sjson_parsed = json.loads(json_data)
            sstrength = 0
            sdexterity = 0
            sconstitution = 0
            sintelligence = 0
            swisdom = 0
            scharisma = 0
            if 'str' in sjson_parsed:
                sstrength = int(sjson_parsed['str'])
                sub['str'] = sstrength
            if 'dex' in sjson_parsed:
                sdexterity = int(sjson_parsed['dex'])
                sub['dex'] = sdexterity
            if 'con' in sjson_parsed:
                sconstitution = int(sjson_parsed['con'])
                sub['con'] = sconstitution
            if 'int' in sjson_parsed:
                sintelligence = int(sjson_parsed['int'])
                sub['int'] = sintelligence
            if 'wis' in sjson_parsed:
                swisdom = int(sjson_parsed['wis'])
                sub['wis'] = swisdom
            if 'cha' in sjson_parsed:
                scharisma = int(sjson_parsed['cha'])
                sub['cha'] = scharisma

            context['subrace_mods'][subrace.name] = sub
            context['subraceFeatures'][subrace.name] = SubraceFeatures.objects.filter(subrace = subrace)



        print('json_parsed = '+str(json_parsed))
        print('stre = '+str(strength))
        print('cons = '+str(constitution))
        print('raceFeatures =' + str(context['raceFeatures']))
        print('subraces =' + str(context['subraces']))
        print('subrace_mods =' + str(context['subrace_mods']))
        return context

class WeaponListView(generic.ListView):
    model = Weapon

class WeaponDetailView(generic.DetailView):
    model = Weapon

    def get_context_data(self, **kwargs):
        context = super(WeaponDetailView, self).get_context_data(**kwargs)
        string = context['weapon'].properties
        property_list = [x.strip() for x in string.split(',')]
        context['properties'] = Properties.objects.filter(name = 'asfhndikjahghndndjndfndjfndjfnksdnfdskjnf')
        for x in property_list:
            context['properties'] = context['properties']|Properties.objects.filter(name = x)
        print('properties'+str(context['properties']))
        return context



class SpellListView(generic.ListView):
    model = Spell

class SpellDetailView(generic.DetailView):
    model = Spell

    def get_context_data(self, **kwargs):
        context = super(SpellDetailView, self).get_context_data(**kwargs)
        context['classes'] = CharacterClassSpellList.objects.filter(spell_list = context['spell'])
        context['subclasses'] = CharacterSubclassSpellList.objects.filter(spell_list = context['spell'])

        print('properties'+str(context['classes']))
        return context



class CharacterListView(LoginRequiredMixin,generic.ListView):
    model = Character
    template_name ='char_list.html'
    paginate_by = 10



    def get_queryset(self):
        return Character.objects.filter(username=self.request.user)


class CharacterDetailView(generic.DetailView):
    model = Character
    template_name ='test_for_alan.html'

    def get_context_data(self, **kwargs):
        context = super(CharacterDetailView, self).get_context_data(**kwargs)
        context['race'] = context['character'].race
        return context


from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Armor

# @login_required ?
class ArmorCreate(CreateView):
    model = Armor
    fields = '__all__'
    labels = { 'name':('Armor Name'), 'is_stealth':('Stealth'), }
    initial = {'armor_bonus':0, 'max_dexterity':0, 'is_stealth':False, 'weight':0, 'gold':0, 'silver':0, 'copper':0, 'required_strength':0, 'max_dexterity':0}
    required = {'required_materials':False,} # maybe also not require required_strength and max_dex?
    success_url = reverse_lazy('armors')

class ArmorUpdate(UpdateView):
    model = Armor
    exclude = ['name'] # because I assume updating name might cause problems with url, if not, do field = '__all__'
    success_url = reverse_lazy('armors')

class ArmorDelete(DeleteView):
    model = Armor
    success_url = reverse_lazy('armors')



    # name = models.CharField(default = '', primary_key = True, max_length = 100, help_text = "Enter the name of the armor")
    # armor_bonus = models.SmallIntegerField(default= 0, help_text="Enter the armor bonus for this item in pounds.")
    # max_dexterity =  models.SmallIntegerField(default= 0, help_text="Enter the maximum amount of bonus AC from dex modifier.")
    # is_stealth = models.BooleanField(default = False, help_text="Is the armor stealthy?")
    # #Units: Pounds (lbs)
    # weight = models.SmallIntegerField(default= 0, 	 help_text="Enter the weight for this item in pounds.")
    # gold = models.IntegerField(default=0, help_text="Enter the gold-price component for this armor")
    # silver = models.IntegerField(default=0, help_text="Enter the silver-price component for this armor")
    # copper = models.IntegerField(default=0, help_text="Enter the copper-price component for this armor")
    # required_strength = models.SmallIntegerField(default= 0, help_text="Enter the required strength to use this armor.")
    # required_materials = models.CharField(default = "", max_length = 10000, help_text = "Enter the required materials to cast this spell in JSON format.")

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]
def get_health(request,stub):
    data = {"Hitdie" : CharacterClass.objects.filter(name = stub)[0].hitpoints}
    return JsonResponse(data)

def get_skills(request , cname) :
    data = {"skills" : CharacterClass.objects.filter(name = cname)[0].skill_list}
    return JsonResponse(data)

def get_spells(request,cname,lvl):
    with connection.cursor() as cursor:
        cursor.execute("SELECT dndpal_characterclassspelllist.ranking , dndpal_spell.name , dndpal_spell.spell_level FROM dndpal_characterclassspelllist, dndpal_spell  WHERE dndpal_characterclassspelllist.spell_list_id = dndpal_spell.name AND dndpal_characterclassspelllist.character_class_id = %s AND dndpal_characterclassspelllist.required_level > 0 AND dndpal_characterclassspelllist.required_level <= %s" , [cname , lvl])
        row = dictfetchall(cursor)
    return JsonResponse(row,safe = False)

def get_cantrip(request,cname):
    with connection.cursor() as cursor:
        cursor.execute("SELECT dndpal_characterclassspelllist.ranking , dndpal_spell.name , dndpal_spell.spell_level FROM dndpal_characterclassspelllist, dndpal_spell  WHERE dndpal_characterclassspelllist.spell_list_id = dndpal_spell.name AND dndpal_characterclassspelllist.character_class_id = %s AND dndpal_characterclassspelllist.required_level = 0 " , [cname])
        row = dictfetchall(cursor)
    return JsonResponse(row,safe = False)

def get_features(request,cname,lvl):
    qs = CharacterClassFeatures.objects.all().filter(character_class = cname).filter(required_level = lvl)
    qs_json = serializers.serialize('json', qs)
    return JsonResponse(qs_json,safe = False)

def get_abilites(request,cname,lvl):
    qs = CharacterClassFeatures.objects.all().filter(character_class = cname).filter(feature_type = "Ability").filter(required_level__lte = lvl)
    qs_json = serializers.serialize('json', qs)
    return JsonResponse(qs_json,safe = False)

def testing_post (request):
    print('*'*50)
    print(request.body)
    print('*'*50)
    return JsonResponse({"data" : 0})
