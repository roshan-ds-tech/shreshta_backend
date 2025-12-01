from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

# ✅ Phone number validator (allows +, and enforces 10–15 digits)
phone_validator = RegexValidator(
    regex=r'^\+?\d{10,15}$',
    message='Enter a valid phone number with at least 10 digits.'
)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(
        max_length=15,
        validators=[phone_validator],
        blank=True
    )
    profile_image = models.ImageField(
        upload_to='profile_images/',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.user.username

# Create your models here.
