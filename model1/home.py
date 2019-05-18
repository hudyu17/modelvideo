from django import forms

class PlayerInput(forms.Form):
	name = forms.CharField(max_length = 30,
		widget = forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Player Name'}))