from django.contrib.auth.models import AbstractUser
from django.db import models
from .manage import UserManager


class User(AbstractUser):
    CREATOR = "CREATOR"
    SUBSCRIBER = "SUBSCRIBER"

    ROLE_CHOICES = (
        (CREATOR, "Creator"),
        (SUBSCRIBER, "Subscriber"),
    )
    profile_photo = models.ImageField(upload_to='uploads/')
    role = models.CharField(max_length=30, choices=ROLE_CHOICES)

    USERNAME_FIELD = "username"
    objects = UserManager()

    def __str__(self):
        return str(self.username)

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
