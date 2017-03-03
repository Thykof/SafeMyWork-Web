from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.generic import DetailView


from smwWeb.forms import LoginForm, SigninForm, SettingsFileForm
from smwWeb.models import Account, SettingsFile

# Create your views here.

def home(request):
    return render(request, 'index.html')

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
            return render(request, 'login.html', locals())


def logout_view(request):
    logout(request)
    return redirect(reverse(login_view))

def signin_view(request):
    error = False

    if request.method == "POST":
        form = SigninForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            password_nd = form.cleaned_data["password_nd"]
            email = form.cleaned_data["email"]

            duplicate = True
            for user in User.objects.all():
                if user.username.lower() == username.lower() or user.email == email:
                    duplicate = False

            if password == password_nd and duplicate:
                user = User.objects.create_user(username, email, password)
                account = Account(user=user)
                account.save()

                user = authenticate(username=username, password=password)
                login(request, user)

                return redirect(member_account)
            else:
                error = True
        else:
            error = True
    else:
        form = SigninForm()

    return render(request, 'signin.html', locals())

def say_hello(request):
    if request.user.is_authenticated():
        return HttpResponse("Hi, {0} !".format(request.user.username))
    return HttpResponse("Hi, anonymous.")

@login_required()
def member_account(request):
    return render(request, 'member.html', locals())

@login_required()
def upload_settings(request):
    error = False
    if request.method == "POST":
        form = SettingsFileForm(request.POST, request.FILES)
        if form.is_valid():
            settings = form.cleaned_data['settings']

            settings_file = SettingsFile(settings_file=settings, account=request.user.account)
            settings_file.save()
            return redirect('home')
        else:
            error = True
    else:
        form = SettingsFileForm()
    return render(request, 'upload.html', locals())
