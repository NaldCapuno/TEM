from django.shortcuts import render, redirect
from .forms import UserInfoForm
from .models import UserInfo

# Create your views here.
def home(response):
    return render(response, 'main/home.html', {})

def account(response):
    user_info = UserInfo.objects.first()  # Fetch the existing user_info record if it exists

    if response.method == 'POST':
        if user_info:
            form = UserInfoForm(response.POST, instance=user_info)
        else:
            form = UserInfoForm(response.POST)
        
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        if user_info:
            # If user_info exists, create a new form instance with the existing data
            form = UserInfoForm(instance=user_info)
        else:
            # If user_info doesn't exist, create a new, empty form instance
            form = UserInfoForm()

    return render(response, 'main/account.html', {'form': form, 'user_info': user_info})
    
def card(response):
    return render(response, 'main/card.html', {})