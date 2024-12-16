from django import forms
from .models import albumModel

class albumForm(forms.ModelForm):
    class Meta:
        model = albumModel
        fields = '__all__'
        
        widgets = {
            'release_date': forms.DateInput(attrs={'type': 'date'}),
        }
