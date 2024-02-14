from django.shortcuts import render , redirect

from django.http import HttpResponse

from django.contrib.auth import login , logout , authenticate
from django.contrib import messages
from .forms import SignUpForm , AddRecordForm
from .models import record


# Create your views here.

def home(request):
    #storing records
    records = record.objects.all()
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
        return render(request , 'home.html' , {'records' : records})





def logout_user(request):
    logout(request)
    messages.success(request , "You have been logged out...")
    return redirect('home')


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
        #authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username , password = password)
            login(request , user)
            messages.success(request , "You have been Registered")
            return redirect('home')
    else:
        form = SignUpForm()        
        return render(request , 'register.html' , {'forms' : form})
    
    return render(request , 'register.html' , {'forms' : form})


def expense_record(request , pk):
    if request.user.is_authenticated:
        
        expense_record = record.objects.get(id = pk)
        return render(request , 'expense_record.html' , {'record' : expense_record})
    else :
        return redirect('home')
        

def delete_record(request , pk):
    if request.user.is_authenticated:
        
        object = record.objects.get(id = pk)
    
        if request.method == 'POST':
            object.delete()
            messages.success(request , "The record has been deleted!")
            return redirect('home')
        return render(request , 'delete.html' , {})
    else :
        
        return render(request , 'delete.html' , {})

def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        
        if request.method == 'POST':
            if form.is_valid():
                add_record = form.save()
                messages.success(request , "The record is added!")
                return redirect('home')
        return render (request , 'add.html' , {'form' : form})
    else:
        return redirect('home')
    
def update(request , pk):
    if request.user.is_authenticated:
        current_record = record.objects.get(id = pk)
        form = AddRecordForm(request.POST or None , instance= current_record)
        if form.is_valid():
            form.save()
            messages.success(request , "Records been updated")
            return redirect('home')
        return render (request , 'update.html' , {'form' : form})
    else:
        return redirect('home')