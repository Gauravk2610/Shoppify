from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,  logout
from django.contrib.auth import login as loginn
from django.contrib import messages
from django.contrib.auth.models import User
from shop.models import Order_place

# Create your views here.
def login(request):

    if request.user.is_authenticated is True:
        return redirect("shop/")
    
    return render(request, 'login.html')

def loginhandle(request):

    if request.method == "POST":
        loginusername = request.POST["form-username"]
        loginpassword = request.POST["form-password"]
        user = authenticate(username=loginusername, password=loginpassword)

        print(loginusername)
        if user is not None:
            if user.is_active:
                print("user: {}" .format(user.is_active))
                loginn(request, user)
                messages.success(request, "Welcome Back {}. Successfully Logged In".format(loginusername) )
                return redirect("shop/")
        
        else:
            messages.warning(request, "Invalid Credentials Username or Password not correct")            
            return redirect("/")
    return HttpResponse("Not Found")

def signup(request):
    if request.method == "POST":
        print("DOne")
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        print(username, fname, lname, email, pass1, pass2)

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "Your Shoppify Account Has Been Successfully Created")
        return redirect('/shop')
    else:
        return HttpResponse("404 Not Found")

def logouthandle(request):
    logout(request)
    message = True
    return redirect("/")