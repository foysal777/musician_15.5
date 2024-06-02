from django import forms
from .models import musicModel


class modelForm(forms.ModelForm):
    class Meta:
        model = musicModel
        fields = '__all__' 
  
    