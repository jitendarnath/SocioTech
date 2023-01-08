from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    return render(request, "index.html")


def handleSignup(request):
    if request.method == 'POST':
        # Get the post parameters
        uname = request.POST.get('uname')
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        # Check for errorneous inputs
        # username should be under 10 characters
        if len(uname) > 10:
            messages.error(request, "Username must be under 10 characters.")
            return redirect("/")

        # passwords should match
        if pass1 != pass2:
            messages.error(request, "Passwords do not match.")
            return redirect("/")

        # Create the user 
        myuser = User.objects.create_user(uname, email, pass1)
        myuser.user_name = uname
        myuser.save()
        messages.success(request, "Your account has been successfully created.")
        return redirect("/")
    else:
        return HttpResponse('404 - Not Found')

def handleLogin(request):
    if request.method == 'POST':
        # Get the post parameters
        loginusername = request.POST.get('loginusername')
        loginpassword = request.POST.get('loginpassword')

        user = authenticate(username=loginusername, password=loginpassword)

        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("/") 
        else:
            messages.error(request, "Invalid Credentials, Please try again")
            return redirect("/")
            
    return HttpResponse('404 - Not Found')

def handleLogout(request): 
    logout(request)
    messages.success(request, "Successfully Logged Out")
    return redirect("/") 
