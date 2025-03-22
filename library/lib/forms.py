
from django import forms
 

from .models import FormModel
 

class Formi(forms.ModelForm):

    class Meta:
        model = FormModel
        fields =['title', 'author', 'des', 'img']