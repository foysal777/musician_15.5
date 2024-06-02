from django.shortcuts import render, redirect
from . import forms

# Create your views here.
def album(request):
    if request.method == "POST":
        my_form = forms.albumForm(request.POST)
        if my_form.is_valid():
            my_form.save()
            return redirect ('album')
    
    
    else :
        my_form = forms.albumForm()
    return render(request, 'album.html', {'data' : my_form })
    
    
    
    
    






   


    