from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render

def home_view(request):
    return render(request,'website/index.html')

def about_view(request):
    return render(request,'website/about.html')

def contact_view(request):
    return render(request,'website/contact.html')

def elements_view(request):
    return  render(request,'website/elements.html')