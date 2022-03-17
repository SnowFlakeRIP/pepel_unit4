from django.shortcuts import render, redirect

from mysite.users.forms import UserForm


def index(request):
    return 'hello'


def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
        return '<h1>Готово</h1>'
