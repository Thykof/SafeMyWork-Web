from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Account(models.Model):
    user = models.OneToOneField(User)
    upload_datetime = models.DateTimeField(null=True)

    def __str__(self):
        msg = "Account of {}, last upload:".format(self.user.username) + self.last_upload()
        return msg

    def last_upload(self):
        if self.upload_datetime:
            msg = self.upload_datetime.strftime("%c")
        else:
             msg = "not upload yet."
        return msg
