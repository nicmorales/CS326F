
from django.urls import path, include, re_path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('simple/', views.simple, name='simple'),
    path('profile/', views.profile, name='profile'),
    path('armors/', views.ArmorListView.as_view(), name='armors'),
    path('armor/<str:pk>', views.ArmorDetailView.as_view(), name='armor-detail'),
    path('classes/', views.ClassListView.as_view(), name='classes'),
    path('class/<str:pk>', views.ClassDetailView.as_view(), name='class-detail'),
    path('equipment/', views.EquipmentListView.as_view(), name='equipment'),
    path('equipment/<str:pk>', views.EquipmentDetailView.as_view(), name='equipment-detail'),
    path('races/', views.RaceListView.as_view(), name='races'),
    path('race/<str:pk>', views.RaceDetailView.as_view(), name='race-detail'),
    path('weapons/', views.WeaponListView.as_view(), name='weapons'),
    path('weapon/<str:pk>', views.WeaponDetailView.as_view(), name='weapon-detail'),
    path('spells/', views.SpellListView.as_view(), name='spells'),
    path('spell/<str:pk>', views.SpellDetailView.as_view(), name='spell-detail'),
    path('classes/', views.ClassListView.as_view(), name='classes'),
    path('class/<str:pk>', views.ClassDetailView.as_view(), name='class-detail'),

]
