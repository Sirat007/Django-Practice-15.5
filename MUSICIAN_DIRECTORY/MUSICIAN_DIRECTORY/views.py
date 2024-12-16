from django.shortcuts import render,redirect
from album.models import albumModel

def home(request):
    data = albumModel.objects.all()
    return render(request,'home.html',{'data':data})