from django.conf.urls import url
from django.urls import path, include, re_path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('simple/', views.simple, name='simple'),
    path('profile/', views.profile, name='profile'),
    path('armors/', views.ArmorListView.as_view(), name='armors'),
    path('armor/<str:pk>', views.ArmorDetailView.as_view(), name='armor-detail'),
    path('equipment/', views.EquipmentListView.as_view(), name='equipment'),
    path('equipment/<str:pk>', views.EquipmentDetailView.as_view(), name='equipment-detail'),
    path('races/', views.RaceListView.as_view(), name='races'),
    path('race/<str:pk>', views.RaceDetailView.as_view(), name='race-detail'),
    path('weapons/', views.WeaponListView.as_view(), name='weapons'),
    path('weapon/<str:pk>', views.WeaponDetailView.as_view(), name='weapon-detail'),
    path('spells/', views.SpellListView.as_view(), name='spells'),
    path('spell/<str:pk>', views.SpellDetailView.as_view(), name='spell-detail'),
    path('classes/', views.CharacterClassListView.as_view(), name='classes'),
    path('class/<str:pk>', views.CharacterClassDetailView.as_view(), name='class-detail'),
    path('alan', views.alan, name='alan'),

    #path('armor/custom_form/', views.custom_armor_form, name='custom-armor-form'), # if for already made shit, arnmor/<uuid:pk>/custom_form/ ?
    path('armor/create/', views.ArmorCreate.as_view(), name='armor_create'),
    path('armor/<str:pk>/update/', views.ArmorUpdate.as_view(), name='armor_update'),
    path('armor/<str:pk>/delete/', views.ArmorDelete.as_view(), name='armor_delete'),

	#ajax all the fucking ajax
    url(r'^ajax/get_health/(?P<stub>[-\w]+)$', views.get_health, name='get_health'),
	url(r'^ajax/get_skills/(?P<cname>[-\w]+)$', views.get_skills),
]


# Niko's pages:
urlpatterns += [
    path('guided/', views.guided, name='guided'),
]


urlpatterns += [
    path('mycharacters/', views.CharacterListView.as_view(), name='my-characters'),
    path('character/<int:pk>', views.CharacterDetailView.as_view(), name ='character-detail'),
]