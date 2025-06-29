from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
# Create your views here.

def loginfn(request):
    eror=None
    if request.POST:
        username=request.POST['username']
        password=request.POST['password']
        print(username,password)
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('display')
        else:
            eror="invalid credentials"
    return render(request,'login.html',eror)

def logoutfn(request):
    logout(request)
    return redirect('login')
def signup(request):
    if request.POST:
        username=request.POST['username']
        password=request.POST['password']
        print(username,password)
        try:

            user=User.objects.create_user(username=username,password=password)
        except:
            print("user already exists")
        print("user created")
    return render(request,'signup.html')