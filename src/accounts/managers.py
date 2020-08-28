from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _
from accounts import models


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, password, user_type, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        # user_type = self.user_type
        user = self.model(email=email, user_type = user_type, **extra_fields)
        user.set_password(password)
        user.save()
        if user_type == 1:
            models.Patient.objects.create(user = user)
            print("patient user created")
        if user_type == 2:
            models.Doctor.objects.create(user = user)
            print("Doctor user created")
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, user_type=3, **extra_fields)
