from django.shortcuts import render, redirect
from musician_app.models import musicModel
from musician_app.forms import modelForm
from album_app import models
from musician_app import models
from album_app.forms import albumForm
from musician_app.forms import modelForm

def home(request):
    return render(request, 'home.html')

def database(request):
    combined_data = musicModel.objects.select_related('musicians').all()
    
    data_list = [{
        'id': item.musician_id,
        'musician_name': f"{item.first_name} {item.last_name}",
        'email': item.email,
        'instrument': item.instrument,
        'album_name': item.musicians.Album_name,
        'album_rating': item.musicians.Album_Rating,
        'release_date': item.musicians.Album_release_Date,
    } for item in combined_data ]
    
    return render(request, 'database.html', {'data': data_list})

def edit_album(request, id):
    album = models.albumModel.objects.get(pk=id)
    form = albumForm(instance=album)
    if request.method == "POST":
        form = albumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('database')
    
    return render(request, 'album.html', {'data': form})

def edit_name(request, id):
    musician = models.musicModel.objects.get(pk=id)
    form = modelForm(instance=musician)
    if request.method == "POST":
        form = modelForm(request.POST, instance=musician)
        if form.is_valid():
            form.save()
            return redirect('database')
    
    return render(request, 'musician.html', {'data': form})

def delete_post(request, id):
    musician = models.musicModel.objects.get(pk=id)
    musician.delete()
    return redirect('database')
