from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserInfoForm
from .models import UserInfo
from django.contrib.auth.models import User

# Create your views here.
def home(response):
    return render(response, 'main/home.html', {})

def account(response):
    if response.method == 'POST':
        form = UserInfoForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect('/account')
    else:
        form = UserInfoForm()
    return render(response, 'main/account.html', {'form': form})

def card(response):
    return render(response, 'main/card.html', {})