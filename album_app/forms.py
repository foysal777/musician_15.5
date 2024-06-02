from django import forms
from .models import albumModel


class albumForm(forms.ModelForm):
    class Meta:
        model = albumModel
        fields = '__all__' 
        
  
    