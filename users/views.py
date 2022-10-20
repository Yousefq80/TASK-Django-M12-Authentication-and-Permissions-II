from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import RegistrationForm,LoginForm
from django.contrib.auth import login,logout,authenticate




def register_user(request):
    form = RegistrationForm()
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)

            user.set_password(user.password)
            user.save()

            login(request, user)
            # Where you want to go after a successful signup
            return redirect("home")
    context = {
        "form": form,
    }
    return render(request, "register.html", context)
# Create your views here.


def logout_view(request):
    logout(request)
    return redirect("success-page")

def login_user(request):
    form = login_user()
    if request.method == "POST":
        form = login_user(request.POST)
        if form.is_valid():

            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            auth_user = authenticate(username=username, password=password)
            if auth_user is not None:
                login(request, auth_user)
                
                return redirect("home")

    context = {
        "form": form,
    }
    return render(request, "login.html", context)