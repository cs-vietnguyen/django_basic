from django.db import models
from django.contrib.auth.hashers import make_password

from Common.domain.models import BaseModel
from Common.utils import pkgen
from AccountManagement.domain.contants import ADMIN, USER


class AccountTypeChoises(models.IntegerChoices):
    ADMIN = ADMIN, "Admin"
    USER = USER, "User"


class Account(BaseModel):
    id = models.UUIDField(max_length=40, primary_key=True, default=pkgen)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    username = models.CharField(max_length=50, null=True, blank=True, unique=True)
    password = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True, unique=True)
    dob = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    avatar = models.URLField(max_length=150, null=True, blank=True)
    type = models.IntegerField(
        default=AccountTypeChoises.USER, choices=AccountTypeChoises.choices
    )
    status = models.IntegerField(default=1)

    class Meta:
        db_table = "account"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super(Account, self).save(*args, **kwargs)
