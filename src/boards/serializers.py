from django.conf import settings

from rest_framework import serializers
# from accounts.models import CustomUser
from .models import Boards, Picture

class BoardSerializer(serializers.ModelSerializer):

    extras = serializers.JSONField(required= False)
    picture = serializers.ImageField(required = False)

    class Meta:
        model = Boards
        fields = ['idx','title', 'extras', 'picture']

class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Picture
        fields = ['idx', 'image']