from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models


class User(AbstractBaseUser):
    uname = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=256)
    email = models.CharField(max_length=256)

    USERNAME_FIELD = 'uname'

    class Meta:
        db_table = 'Users'

    def __str__(self):
        return self.uname
