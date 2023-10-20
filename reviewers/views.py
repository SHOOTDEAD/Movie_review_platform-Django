from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import UserForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# Render Home_Page
def home_page(req):
    return render(req, "home_page.html", context={"status": req.session.get("status")})

#Signup
def signup(req):
    form = UserForm(req.POST or None)
    if req.method == "POST":
        form.is_valid()
        data = form.cleaned_data
        #Checking if user exist
        if User.objects.filter(username=data["username"]):
            return render(req, "signup.html", context={"form": form, "status": 1})
        else:
            #Creating new user
            user = User.objects.create_user(**data)
            user.save()
            req.session["status"] = 3
            return redirect("home")

    return render(req, "signup.html", context={"form": form})

#Login
def loginy(req):
    form = LoginForm(req.POST or None)
    req.session["status"] = 1
    if req.method == "POST":
        form.is_valid()
        data = form.cleaned_data
        #Authenticating user
        user = authenticate(req, username=data["username"], password=data["password"])

        
        if user:
            login(req, user)

            return redirect(reverse("movies"))
        return render(req, "login.html", context={"status": 2, "form": form})
    return render(
        req, "login.html", context={"form": form, "status": req.session["status"]}
    )

#Logout
def logouty(req):
    logout(req)
    req.session["status"] = 2

    return redirect("home")
