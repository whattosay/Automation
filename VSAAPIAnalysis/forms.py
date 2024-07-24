from django import forms
from .models import User, App, Group

class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['name']
		widgets = {
			'name': forms.TextInput(attrs={'class': 'autocomplete'}),
		}

class AppForm(forms.ModelForm):
	class Meta:
		model = App
		fields = ['name']
		widgets = {
			'name': forms.TextInput(attrs={'class': 'autocomplete'}),
		}

class GroupForm(forms.ModelForm):
	class Meta:
		model = Group
		fields = ['name']
		widgets = {
			'name': forms.TextInput(attrs={'class': 'autocomplete'}),
		}