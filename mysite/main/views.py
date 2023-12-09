from django.shortcuts import render, redirect
from .forms import UserInfoForm
from .models import UserInfo

# Create your views here.
def home(response):
    return render(response, 'home.html', {})

def my_account(response):
    user_info = UserInfo.objects.get(user=response.user)
    return render(response, 'my-account.html', {'user_info': user_info})

def my_library_card(response):
    user_info = UserInfo.objects.get(user=response.user)
    return render(response, 'my-library-card.html', {'user_info': user_info})

def account_information(response):
    if response.method == 'POST':
        form = UserInfoForm(response.POST, response.FILES)
        if form.is_valid():
            form.save()
            return redirect('/my-account')
    else:
        form = UserInfoForm(initial={'user': response.user})

    return render(response, 'account-information.html', {'form': form})
