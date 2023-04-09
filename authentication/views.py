from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

# Create your views here.

class VRegister(View):

    def get(self, request):
        form = UserCreationForm()
        return render(request, "registration/registration.html", {"form":form})

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("Home")
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
            return render(request, "registration/registration.html", {"form":form})
        
def log_out(request):
    logout(request)

    return redirect("Home")

def log_in(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            u_name = form.cleaned_data.get("username")
            u_psswrd = form.cleaned_data.get("password")
            user = authenticate(username=u_name, password=u_psswrd)
            if user is not None:
                login(request, user)
                return redirect("Home")
            else:
                messages.error(request, "User not valid")
        else:
            messages.error(request, "Info not valid")
    
    form = AuthenticationForm()
    return render(request, "login/login.html", {"form":form})