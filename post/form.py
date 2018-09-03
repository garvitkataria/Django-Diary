from django import forms

class NameForm(forms.Form):
	title = forms.CharField(max_length=50)
	body = forms.CharField(widget=forms.Textarea)