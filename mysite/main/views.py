from django.shortcuts import render, redirect
from .forms import UserInfoForm
from .models import UserInfo

# Create your views here.
def home(response):
    return render(response, 'main/home.html', {})

def my_account(response):
    user_info = UserInfo.objects.get(user=response.user)
    return render(response, 'main/my-account.html', {'user_info': user_info})

def my_library_card(response):
    return render(response, 'main/my-library-card.html', {})

def update_account(response):
    if response.method == 'POST':
        form = UserInfoForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect('/my-account')
    else:
        form = UserInfoForm(initial={'user': response.user})

    return render(response, 'main/update-account.html', {'form': form})
