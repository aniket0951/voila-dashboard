from django.contrib import admin
from django.urls import path
from voilaDashboard.views import loginUser, validateCredentials

urlpatterns = [
    path('loginUser', loginUser , name='loginUser'),
    path('validateCredentials/', validateCredentials, name='validateCredentials')
]