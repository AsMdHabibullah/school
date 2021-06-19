# from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def dep_view(request):
    return HttpResponse("Hi, I'm from department!")
