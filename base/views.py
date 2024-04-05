from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# function base views


def home(request):
  return HttpResponse("Home page")


def room(request):
  return HttpResponse("Rooms Page")
