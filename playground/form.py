from django.forms import ModelForm
from .models import Room 

class RoomForm(ModelForm): 
    class Meta: 
        model = Room 
        fields = '__all__'
        #or you can add a list of fields you want to include 
        #fields = ['name', 'description', 'topic']
        exclude = ['host','participants']
