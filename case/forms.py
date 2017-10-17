from django import forms
from django.contrib.auth.models import User, Group
from django.forms import CheckboxInput, Textarea 

from .models import Product, Forcast




class ProductForm(forms.ModelForm):
	class Meta:
		model = Product 
		fields = '__all__'
		exclude = ['inventory_cost']


class ForcastForm(forms.ModelForm):
	class Meta:
		model = Forcast
		fields = '__all__'