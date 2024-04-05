from django.shortcuts import render

from .models import Room

# Create your views here.
from django.http import HttpResponse

# function base views

# rooms = [
#   {'id': 1, 'name': 'Lets learn python!'},
#   {'id': 2, 'name': 'Build with Evans!'},
#   {'id': 3, 'name': 'Backend Engineer!'},
# ]

def home(request):
  rooms = Room.objects.all()
  context = {'rooms': rooms}
  return render(request, 'base/home.html', context)


def room(request, pk):
  room = Room.objects.get(id=pk)
  context = {'room': room}
  return render(request, 'base/room.html', context)
