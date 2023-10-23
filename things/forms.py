from .models import Thing
from django import forms
"""Forms of the project."""

# Create your forms here.
class ThingForm(forms.ModelForm):
    class meta: 
        model = Thing
        fields = ['name', 'description','quantity']
        #widgets = {'description':forms.Textarea()}
        #quantity = forms.NumberInput()

 