from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Room

class RoomForm(ModelForm):
  class Meta:
    model = Room
    fields = '__all__'
    exclude = ['host', 'participants']


# class RoomForm(ModelForm):
#     class Meta:
#         model = Room
#         exclude = ["created"]

class UserForm(ModelForm):
  class Meta:
    model = User
    # fields = '__all__'
    fields = ['username', 'email']
