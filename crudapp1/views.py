from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets,views 
from crudapp1.models import Person

from .forms import CreatePersonForm, CreateUserForm, LoginForm, UpdatePersonForm


def registerform(request):

    form = CreateUserForm()

    if request.method == "POST":

        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect("")
    return render(request, "register.html", {"form": form})


def loginform(request):

    form2 = LoginForm()
    # form3 = CreateUserForm()

    if request.method == "POST":

        form = LoginForm(request, data=request.POST)

        username = request.POST["username"]
        password = request.POST.get("password")
        user = auth.authenticate(password=password, username=username)
        if user is not None:
            auth.login(request, user)
            return redirect("dashboard")

        else:
            user is None

            messages.info(request, "this user is not regiastered yet")
            return redirect("register")

    return render(request, "login.html", {"form2": form2})


def user_logout(request):

    auth.logout(request)
    return redirect("login")


def index(request):

    person = Person.objects.all()
    return render(request, "index.html", {"p" "ersons": person})


def register(request):

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        password_confirm = request.POST["password-confirm"]

        if password == password_confirm:

            if User.objects.filter(username=username).exists():
                messages.info(request, "this username already exist")
                return redirect("register")

            # since email is not part of the data we will be needing for our login i commented it out

            # elif User.objects.filter(email= email).exists():
            #     messages.info(request,'this email is already in use')
            #     return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                messages.success(request,'user has been registered successfully')
                return redirect("login")
        elif password != password_confirm:
            messages.info(request, "ensure the password correlate with the first one ")
            return redirect("register")

    return render(request, "register.html")


def login(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        # username =  request.POST['username']
        # password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("dashboard")
        # if user is not None and password != password:
        #     return redirect('login')
        else:
            user is None
            messages.info(request, "this user is not registered")
            return redirect("register")
    return render(request, "login.html")


@login_required(
    login_url="login"
)  # this line of code ensures that only user thta is authenticated or logged in  can have access to sees the dashboard if you are able too login to the backend  of the website it means ure are an admin ao if any other user logged in into the website initially , if you refresh the sebsite , it will log the user out and log you in but if you now logout of the backend after this , the it will redirect us to the loginpage again
def dashboard(request):

    person = Person.objects.all()
    return render(request, "dashboard.html", {"persons": person})


def logout(request):
    #  user = auth.authenticate(username=username,password=password)
    auth.logout(request)
    return redirect("/")


def details(request, pk):
    if pk:
        # try:
        detail = Person.objects.get(id=pk)
        # except Person.DoesNotExist:
        # messages.error
        return render(request, "details.html", {"detail": detail})


def create(request):

    form = CreatePersonForm()

    if request.method == "POST":

        form = CreatePersonForm(request.POST)
        if form.is_valid():
            form.save()
    
            return redirect("dashboard")

    return render(request, "create-record-django.html", {"form": form})


def update(request, pk):

    record = Person.objects.get(id=pk)
    form = UpdatePersonForm(instance=record)

    if request.method == "POST":

        form = UpdatePersonForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            messages.success(request,'record has been updated successfully')
            return redirect("dashboard")

    return render(request, "update.html", {"form": form, "id": pk})


def delete(request, pk):

    record = Person.objects.get(id=pk)
    messages.success(request,'record has been deleted')
    record.delete()

    return redirect("dashboard")
