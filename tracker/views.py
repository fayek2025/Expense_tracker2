from django.shortcuts import render , redirect

from django.http import HttpResponse

from django.contrib.auth import login , logout , authenticate
from django.contrib import messages


# Create your views here.

def home(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request , username = username , password = password)

        if user is not None: #it means that user is authenticated or user exists
            login(request , user)
            messages.success(request , "You have been logged in successfully!")
            return redirect('home')
        else:
            messages.success(request , "You made some error1")
            return redirect('home')
            

    else :
        return render(request , 'home.html' , {})





def logout_user(request):
    logout(request)
    messages.success(request , "You have been logged out...")
    return redirect('home')