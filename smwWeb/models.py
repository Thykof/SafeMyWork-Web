from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Account(models.Model):
    user = models.OneToOneField(User)

    def __str__(self):
        return "Account of {0}".format(self.user.username)

class SettingsFile(models.Model):
    account = models.OneToOneField(Account)
    settings_file = models.FileField(upload_to='settings/')
