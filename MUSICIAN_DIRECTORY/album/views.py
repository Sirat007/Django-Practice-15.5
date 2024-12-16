from django.shortcuts import render,redirect
from . import forms
from . import models

# Create your views here.

def album(request):
    if request.method == 'POST':
        form = forms.albumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = forms.albumForm()
    return render(request,'album.html',{'form':form})


def edit(request,id):
    album = models.albumModel.objects.get(pk=id)
    album_form = forms.albumForm(instance = album)
    if request.method == "POST":
        album_form = forms.albumForm(request.POST, instance= album)
        if album_form.is_valid():
            album_form.save()
            return redirect('homepage')
    
    return render(request,'album.html',{'form':album_form})

def delete(request,id):
    album = models.albumModel.objects.get(pk=id)
    album.delete()
    return redirect('homepage')