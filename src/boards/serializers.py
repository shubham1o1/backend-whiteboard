from django.conf import settings

from rest_framework import serializers
# from accounts.models import CustomUser
from .models import Boards

class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boards
        fields = ['idx','title','user', 'extras', 'picture']

    