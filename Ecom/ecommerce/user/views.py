from django.shortcuts import render, redirect
from .forms import UserRegistrationForm,CustomerMoreForm, LoginForm

from .models import CustomerLogin
#importing for user CustomerLogin
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.

def register(request):
    user_form = UserRegistrationForm(request.POST)
    more_form = CustomerMoreForm(request.POST)
    context = {'user_form': user_form, 'more_form':more_form}
    template = 'auth/registration.html'
    return render(request,template, context)


def register_process(request):

    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        more_form = CustomerMoreForm(request.POST)
        # context = {'user_form': user_form, 'more_form':more_form}

        if user_form.is_valid() and more_form.is_valid():
            user = user_form.save()
            #hashing the  password declared in settings.py
            user.set_password(user.password)
            user.save()

            add_form = more_form.save(commit = False) #commit to eliminate the override of user
            add_form.user = user

            add_form.save()
            return HttpResponseRedirect(reverse('home'))

    else:
        user_form = UserRegistrationForm()
        more_form = CustomerMoreForm()
        # template = 'auth/registration.html'
        context = {'user_form': user_form, 'more_form':more_form}
        return render(request, 'auth/registration.html', context)


def login_page(request):
    login_customer = LoginForm(request.POST)
    context = {'login_customer': login_customer}
    template= 'auth/login.html'
    return render(request, template, context)


def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        #automatically authenticate the user
        user = authenticate(username = username, password= password)

        #checks if the user exists
        if user:
            login(request,user)
            return HttpResponseRedirect(reverse('cart'))
        else:
            form = LoginForm(request.POST)
            error_message = "Username and Password do not match!!"
            context = {'error_message':error_message,'form':form}
            template = 'auth/login.html'
            return render(request,template,context)
    else:
        user_form = UserRegistrationForm(request.POST)
        more_form = CustomerMoreForm(request.POST)
        context = {'user_form': user_form, 'more_form':more_form}
        return render(request,'auth/registration.html',context)

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))
