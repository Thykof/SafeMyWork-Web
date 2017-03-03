from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

from django.http import HttpResponse


from smwWeb.forms import LoginForm

# Create your views here.

def login_view(request):
    error = False

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect(member_account)
            else:
                error = True

                return render(request, 'login.html', locals())
    else:
        if request.user.is_authenticated:
            return redirect(member_account)
        else:
            form = LoginForm()
            print('new form')
            return render(request, 'login.html', locals())


def logout_view(request):
    logout(request)
    return redirect(reverse(login_view))

def signin_view(request):
    return render(request, 'index.html')

def say_hello(request):
    if request.user.is_authenticated():
        return HttpResponse("Hi, {0} !".format(request.user.username))
    return HttpResponse("Hi, anonymous.")

@login_required()
def member_account(request):
    return render(request, 'member.html', locals())
