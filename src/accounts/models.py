from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from accounts.managers import CustomUserManager
import uuid 

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        (1, 'general'),
        (2, 'admin')
    )

    user_type = models.PositiveSmallIntegerField(
        choices=USER_TYPE_CHOICES)
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    objects = CustomUserManager()

    is_premium = models.BooleanField(
        _('premium status'),
        default=False,
        help_text=_(
            'Designates whether the user is premium or not'
        ),
    )

    duration = models.IntegerField(default=1) 

    def __str__(self):
        return self.email



