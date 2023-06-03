from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def home_page(request):
    return render (request,'home.html')


def signup_page(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')

        if(password1!=password2):
            return HttpResponse('Please Enter Same Password')
        else:

            my_user=User.objects.create_user(uname,email,password1)
            my_user.save()
            return redirect('login')

    return render(request,'signup.html')


def login_page(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render(request, 'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')     