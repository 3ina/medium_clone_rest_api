from django.db import models
import  uuid
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django.utils import timezone
from .managers import CustomUserManager
from django.utils.translation import gettext_lazy as _


class User(AbstractBaseUser, PermissionsMixin):
    pkid = models.BigAutoField(primary_key=True,editable=False),
    id = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(verbose_name=_('First Name'), max_length=50)
    last_name = models.CharField(verbose_name=_('Last Name'), max_length=50)
    email = models.EmailField(verbose_name=_('Email Address'), unique=True,db_index=True),
    is_active = models.BooleanField(default=True),
    is_staff = models.BooleanField(default=False),
    date_joined = models.DateTimeField(default=timezone.now),

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["first_name","last_name"]
    objects = CustomUserManager()

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def __str__(self):
        return self.first_name

    @property
    def full_name(self):
        return f"{self.first_name.title()} {self.last_name.title()}"

