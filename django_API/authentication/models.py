from django.db import models
from django.contrib.auth.models import AbstractUser

GENDER_CHOICES = (
    ('male', 'Male'),
    ('female', 'Female'),
    ('other', 'Other'),
)


class User(AbstractUser):
    first_name = models.CharField(
        max_length=30,
    )
    last_name = models.CharField(
        max_length=30,
    )
    email = models.EmailField(
        unique=True,
    )
    address = models.CharField(
        max_length=200,
    )
    phone_number = models.IntegerField(
        help_text='Enter 11 digits phone number',
        null=True,
        blank=True
    )
    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES)

