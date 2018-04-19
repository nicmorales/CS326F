from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
from .models import *

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
        context['raceFeatures'] = RaceFeatures.objects.all()

        
        context['subraces'] = Subrace.objects.all()

        print('lengthofrace: '+str(context['race'].name));
        print('parent: '+str(context['raceFeatures'][0].race));
        return context

class WeaponListView(generic.ListView):
    model = Weapon

class WeaponDetailView(generic.DetailView):
    model = Weapon

class SpellListView(generic.ListView):
    model = Spell

class SpellDetailView(generic.DetailView):
    model = Spell

class ClassListView(generic.ListView):
    model = CharacterClass

class ClassDetailView(generic.DetailView):
    model = CharacterClass


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
    # weight = models.SmallIntegerField(default= 0, help_text="Enter the weight for this item in pounds.")
    # gold = models.IntegerField(default=0, help_text="Enter the gold-price component for this armor")
    # silver = models.IntegerField(default=0, help_text="Enter the silver-price component for this armor")
    # copper = models.IntegerField(default=0, help_text="Enter the copper-price component for this armor")
    # required_strength = models.SmallIntegerField(default= 0, help_text="Enter the required strength to use this armor.")
    # required_materials = models.CharField(default = "", max_length = 10000, help_text = "Enter the required materials to cast this spell in JSON format.")