from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('prep/', views.meal_prep, name='prep'),
    path('grocery/', views.grocery_list, name='grocery'),
    path('quick/', views.quick_meals, name='quick'),
    path('bakes/', views.bakes, name='bakes'),
    path('lunch/', views.lunch, name='lunch'),
    path('desserts/', views.desserts, name='desserts'),
    path('about/', views.about_us, name='about'),
    path('cakes/', views.cakes, name='cakes'),
    path('cookies/', views.cookies, name='cookies'),
    path('scones/', views.scones, name='scones'),
    path('donuts/', views.donuts, name='donuts'),
    path('muffins/', views.muffins, name='muffins'),
    path('rolls/', views.rolls, name='rolls'),
    path('breads/', views.breads, name='breads'),
]
