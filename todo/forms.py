from django import forms


class TodoForm(forms.Form):
    new_name = forms.CharField(max_length=50)
    new_img = forms.ImageField()
