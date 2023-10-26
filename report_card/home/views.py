from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.models import User
from django.contrib import messages


@login_required(login_url="/login")
def home(request):
    peoples = [ 
        {"name": "Ram", "desc": "backend-developer", "age": 15},
        {"name": "Shyram", "desc": "frontend-developer", "age": 31}
    ]
    
    return render(request, "home/home.html", context= {"peoples": peoples, "page": "Home" })


def register_page(request):
    context = {"page": "Register" }
    if request.method == "POST":

        user = User.objects.filter(username=request.POST.get("username"))
        if user.exists():
            messages.info(request, message="Username already taken")
            return redirect("/register/")

        user = User.objects.create(
            first_name=request.POST.get('firstname'),
            last_name=request.POST.get("lastname"),
            username=request.POST.get("username")
        )

        user.set_password(request.POST.get("password"))
        user.save()
        messages.info(request, message="Account successfully created")

        return redirect('/register/')
    return render(request, "home/register.html",context=context)


def login_page(request):
    context = {"page": "login" }

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(f"{password=}")
        if not User.objects.filter(username=username).exists():
            messages.info(request, "User not exists")
            return redirect('/login')

        user = authenticate(username=username, password=password)  
        if user is None:
            messages.info(request, "Invalid password")
            return redirect('/login')
        else:
            login(request, user)
            return redirect("/")    
    return render(request, "home/login.html",context=context)


def logout_page(request):
    logout(request)
    return redirect('/login')
