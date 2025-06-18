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