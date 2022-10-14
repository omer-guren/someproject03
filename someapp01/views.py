from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.

def index(request, id):
    return render(request, "someapp01folder/index.html", {'doublingkey001': float(int(id)**2), 'presentingkey001': int(id)})

def someapp01(request):
    return HttpResponse("someapp01in icindekiler")

def someapp01_details(request, id):
    return render(request, "someapp01folder/killa.html", {'listingkey001':list(id), 'presentingkey001': f'fantastik {id}'})

