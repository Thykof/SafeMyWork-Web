from os import path, remove
import datetime

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.core.files.storage import default_storage
from django.core.files import File
from django.conf import settings

from django.http import HttpResponse  # Debug


from smwWeb.forms import LoginForm, SigninForm, SettingsFileForm
from smwWeb.models import Account

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

def say_hello(request):  # Debug
    if request.user.is_authenticated():
        return HttpResponse("Hi, {0} !".format(request.user.username))
    return HttpResponse("Hi, anonymous.")

@login_required()
def member_account(request):
    last_upload = request.user.account.last_upload()
    return render(request, 'member.html', locals())

@login_required()
def upload_settings(request):
    error = False
    if request.method == "POST":
        form = SettingsFileForm(request.POST, request.FILES)
        if form.is_valid():
            dest = path.join(settings.MEDIA_ROOT, 'settings', 'config_' + request.user.username + '.yml')

            if not default_storage.exists(dest):
                print('saving')
                default_storage.save(dest, File(request.FILES['settings']))
            else:
                print('updating')
                default_storage.delete(dest)
                default_storage.save(dest, File(request.FILES['settings']))
                
            request.user.account.upload_datetime = datetime.datetime.now()
            request.user.account.save()
            return redirect('account')
        else:
            error = True
    else:
        form = SettingsFileForm()
    return render(request, 'upload.html', locals())
