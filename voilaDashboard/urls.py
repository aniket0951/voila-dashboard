from django.contrib import admin
from django.urls import path
from voilaDashboard.views import loginUser, validateCredentials, addSubUser

urlpatterns = [
    path('loginUser', loginUser , name='loginUser'),
    path('validateCredentials/', validateCredentials, name='validateCredentials'),
    path('addSubUser/<str:tag>/', addSubUser, name='addSubUser')
]