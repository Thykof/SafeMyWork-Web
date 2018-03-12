"""SafeMyWorkWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin


from smwWeb import views

urlpatterns = [
    url(r'^admin24/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^login/$', views.login_view, name='login'),
   	url(r'^signin/$', views.signin_view, name='signin'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^account/$', views.member_account, name='account'),
    url(r'^upload-settings/$', views.upload_settings, name='upload-settings'),
   	url(r'^download-settings/$', views.download_settings, name='download-settings'),
]
