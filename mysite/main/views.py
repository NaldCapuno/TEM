from django.shortcuts import render, redirect
from .forms import UserInfoForm
from .models import UserInfo

# Create your views here.
def home(response):
    return render(response, 'main/home.html', {})

<<<<<<< HEAD
def my_account(response):
    user_info = UserInfo.objects.get(user=response.user)
    return render(response, 'main/my-account.html', {'user_info': user_info})

def my_library_card(response):
    return render(response, 'main/my-library-card.html', {})

def update_account(response):
=======
def account(response):
    user_info = UserInfo.objects.first()  # Fetch the existing user_info record if it exists

>>>>>>> 978c8f18b62e52ea7d04d21dbc1ac573bb380aed
    if response.method == 'POST':
        if user_info:
            form = UserInfoForm(response.POST, instance=user_info)
        else:
            form = UserInfoForm(response.POST)
        
        if form.is_valid():
            form.save()
            return redirect('/my-account')
    else:
<<<<<<< HEAD
        form = UserInfoForm(initial={'user': response.user})

    return render(response, 'main/update-account.html', {'form': form})
=======
        if user_info:
            # If user_info exists, create a new form instance with the existing data
            form = UserInfoForm(instance=user_info)
        else:
            # If user_info doesn't exist, create a new, empty form instance
            form = UserInfoForm()

    return render(response, 'main/account.html', {'form': form, 'user_info': user_info})
    
def card(response):
    return render(response, 'main/card.html', {})
>>>>>>> 978c8f18b62e52ea7d04d21dbc1ac573bb380aed
