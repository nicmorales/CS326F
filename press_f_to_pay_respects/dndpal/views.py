from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

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

from django.views import generic



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
        context['subrace'] = Subrace.objects.all()
        return context