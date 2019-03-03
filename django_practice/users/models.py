from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django_practice.motorcycles.models import Motorcycle
from django.db import models
import uuid as uuid_lib

class User(AbstractBaseUser, PermissionsMixin):
    object = UserManager()

    uuid = models.UUIDField(default=uuid_lib.uuid4,
                            primary_key=True, editable=False)

    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        unique=True,
        max_length=150,
        validators=[username_validator],
    )

    email = models.EmailField(blank=True)

    own = models.ManyToManyField(Motorcycle)

    is_staff = models.BooleanField(
        verbose_name=('staff status'),
        default=False,
    )
    is_active = models.BooleanField(
        verbose_name=('active'),
        default=True,
    )

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', ]

