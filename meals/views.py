from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'meals/home.html')

def meal_prep(request):
    return render(request, 'meals/prep.html')

def grocery_list(request):
    return render(request, 'meals/grocery.html')

def quick_meals(request):
    return render(request, 'meals/quick.html')

def bakes(request):
    return render(request, 'meals/bakes.html')

def lunch(request):
    return render(request, 'meals/lunch.html')

def desserts(request):
    return render(request, 'meals/desserts.html')

def about_us(request):
    return render(request, 'meals/about.html')

def cakes(request):
    return render(request, 'meals/cakes.html')

def cookies(request):
    return render(request, 'meals/cookies.html')

def scones(request):
    return render(request, 'meals/scones.html')

def donuts(request):
    return render(request, 'meals/donuts.html')

def muffins(request):
    return render(request, 'meals/muffins.html')

def rolls(request):
    return render(request, 'meals/rolls.html')

def breads(request):
    return render(request, 'meals/breads.html')