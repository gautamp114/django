from django.shortcuts import render, redirect
from .forms import RegistrationForm

from django.contrib import auth
from django.http import HttpResponse

from django.contrib import messages


# Create your views here.
def login(request):
    if request.method == 'POST':
        user = auth.authenticate( password=request.POST['password'], username=request.POST['name'])
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            messages.info(request, "Username and password does not match")
    context = {}
    template_name = 'auth/login.html'
    return render(request, template_name, context)

def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    context = {
       'form': form,
        # 'error' : error
    }
    template_name = 'auth/register.html'
    return render(request, template_name, context)

def logout_user(request):
    auth.logout(request)
    return redirect('login')