from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import json
from django.core import serializers

from django.http import JsonResponse

# Create your views here.
from .models import *








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
        'test_for_alan.html',
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

class ClassListView(generic.ListView):
    model = CharacterClass

class ClassDetailView(generic.DetailView):
    model = CharacterClass

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

class SpellListView(generic.ListView):
    model = Spell

class SpellDetailView(generic.DetailView):
    model = Spell

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

def get_health(request,stub):
    data = {"Hitdie" : CharacterClass.objects.filter(name = stub)[0].hitpoints}
    return JsonResponse(data)

def get_skills(request , cname) :
    data = {"skills" : CharacterClass.objects.filter(name = cname)[0].skill_options}
    return JsonResponse(data)

