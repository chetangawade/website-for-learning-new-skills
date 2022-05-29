from django.contrib import admin
from django.urls import path ,include
from Services import views

urlpatterns = [
    path('', views.index,name="index"),
    path('dev/<course>', views.dev,name="dev"),
    path("login" , views.loginUser , name='login'),
    path("sign_up" , views.sign_up, name='sign_up'),
    path("logout" , views.logoutUser , name='logout')
]
