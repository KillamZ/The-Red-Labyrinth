from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext as _


from .managers import PlayerManager


class School(models.Model):
    school = models.CharField(default=None, null=True, max_length=50)

    def __str__(self):
        return f"{self.school}"

class Player(AbstractUser):
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    username = models.CharField(_('username'), max_length=30, unique=True, null=True) # is this team name?
    email = models.CharField(_('email'), max_length=100, unique=True, null=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE, null=True, default='')
    score = models.IntegerField(default=0)
    phone_number = models.CharField(default=None, null=True, max_length=50)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ('first_name', 'last_name','email', 'school', 'phone_number')

    objects = PlayerManager()

    def __str__(self):
        return self.username
