from django.forms import ModelForm
from django import forms
from .models import Login,Contents

class Registrationform(ModelForm):
	full_name=forms.TextInput()
	username=forms.TextInput()

	class Meta:
		model=Login
		fields=['username']

	def __str__(self):
		return f'{self.username}'