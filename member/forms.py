
from django import forms
 
from lib.models import FormModel
from .models import MemberModel
 

class Form(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=FormModel.objects.filter(status=True),empty_label="Select a category",required=True)
    class Meta:
        model = MemberModel
        fields = ['name','category']