from .models import User
from django.forms import ModelForm, TextInput


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['name', 'surname']
        widgets = {
            "name": TextInput(attrs={
                'placeholder': 'Имя'
            }),
            "surname": TextInput(attrs={
                'placeholder': 'Фамилия'
            })
        }