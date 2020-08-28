from django.conf import settings

from rest_framework import serializers
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from accounts.models import CustomUser

from rest_auth.registration.serializers import RegisterSerializer
from rest_auth.models import TokenModel
from rest_auth.serializers import PasswordResetSerializer


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'first_name', 'last_name', 'user_type', 'is_premium', 'duration')

class CustomTokenSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()

    class Meta:
        model = TokenModel
        fields = ('key', 'user', )

class CustomRegisterSerializer(RegisterSerializer):
    USER_TYPE_CHOICES = (
        (1, 'general'),
        (2, 'admin')
    )
    user_type = serializers.ChoiceField(
        choices = USER_TYPE_CHOICES,
        required=True)
    is_premium = serializers.BooleanField()

    duration = serializers.IntegerField(default=1) 
    
    class Meta:
        model = CustomUser

    def get_cleaned_data(self):
        super(CustomRegisterSerializer, self).get_cleaned_data()

        return {
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
            'name': self.validated_data.get('name', ''),
            'user_type': self.validated_data.get('user_type', ''),
            'is_premium': self.validated_data.get('is_premium', ''),
            'duration': self.validated_data.get('duration', ''),
        }

class CustomPasswordResetSerializer(PasswordResetSerializer):
    def get_email_options(self):
        return {
            'subject_template_name': 'account/email/password_reset_key_subject.txt',
            # 'email_template_name': 'account/email/password_reset_key.txt',
            'html_email_template_name': 'account/email/password_reset_email.html',
        }

