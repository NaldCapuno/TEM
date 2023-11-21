from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home-page"),
    path("my-library-card/", views.my_library_card, name="my-libray-card-page"),
    path('my-account/', views.my_account, name='my-account-page'),
    path("update-account/", views.update_account, name="update-account-page"),
]