from django.shortcuts import render, redirect
from .forms import UserInfoForm

# Create your views here.
def home(response):
    return render(response, 'main/home.html', {})

def account(response):
    if response.method == 'POST':
        form = UserInfoForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = UserInfoForm()
    return render(response, 'main/account.html', {'form': form})

def card(response):
    return render(response, 'main/card.html', {})