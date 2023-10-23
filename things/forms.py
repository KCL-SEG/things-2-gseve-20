from django import forms
from .models import Thing
from django.db import models
"""Forms of the project."""

# Create your forms here.
class ThingForm(forms.Form):
    class meta: 
        model = Thing
        fields = ['name', 'description', 'quantity']
        widgets = {'description':forms.Textarea()}
        #quantity = forms.NumberInput()


    
    def save(self):
        super().save(commit=False)
        thing = models.Model.objects.create(
            name=self.cleaned_data.get('name'),
            description=self.cleaned_data.get('description'),
            quantity=self.cleaned_data.get('quantity'),

        )
        return thing

      

 