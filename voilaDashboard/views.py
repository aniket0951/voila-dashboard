from django.shortcuts import redirect, render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from voilaDashboard.models import voila_sub_user
from voilaDashboard.serilizer import serializer
import numpy as np

# Create your views here.
def loginUser(request):
    return render(request, 'login.html')

@csrf_exempt
def validateCredentials(request):
    email = request.GET.get('userEmail')
    password = request.GET.get('userPassword')
    if email != "":
        if email == "aniket@gmail.com":
            return render(request, 'home_screen.html')
        else:
            messages.error(request, "Failed to login you are not authorized user.")
            return redirect('loginUser')    
    else:
        messages.error(request, "Please enter the email, Email is required to login..")
        return redirect('loginUser') 

@csrf_exempt    
def addSubUser(request,tag):
    if tag == "open":
        return render(request, 'AddSubUser.html')    
    elif tag == "add":
        email = request.POST.get('userEmail')
        userName = request.POST.get('userName')
        employeeId = request.POST.get('employeeId')
        password = request.POST.get('password')
        
        chars = np.array(list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'))
        np_codes = np.random.choice(chars,56)
        auth_token = ''.join([val for val in np_codes])
        
        createUser = voila_sub_user.objects.create(username=userName,
                                                   email=email,password=password,
                                                   auth_token=auth_token,employee_id=employeeId)

        if createUser:
            messages.success(request, "New User Added Successfully")
            return render(request, 'home_screen.html')
        else:
            messages.error(request, "Failed to add new user, Please try again")
            return render(request, 'home_screen.html')                                               

