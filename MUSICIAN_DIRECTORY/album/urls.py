from django.urls import path
from . import views

urlpatterns = [
    path('add/',views.album,name='albumPage'),
    path('edit/<int:id>',views.edit,name='edit_album'),
    path('delete/<int:id>',views.delete,name='delete'),
]