from django.shortcuts import redirect, render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages


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
            messages.success(request, "Please enter the email, Email is required to login..")
            return redirect('loginUser')
        else:
            messages.error(request, "Failed to login you are not authorized user.")
            return redirect('loginUser')    
    else:
        messages.error(request, "Please enter the email, Email is required to login..")
        return redirect('loginUser') 
    