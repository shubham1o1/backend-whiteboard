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

    def update(self, obj, validated_data):
        extras = validated_data.pop("extras")

        available_keys = obj.extras.keys()

        for key in extras:
            obj.extras.append({"key": extras[key]})

        obj.save()
        obj.update(validated_data)
        return obj

'''
class CustomRegisterSerializer(serializers.ModelSerializer):

    extras = serializers.JSONField(required= False)
    picture = serializers.ImageField(required = False)

    class Meta:
        model = Boards

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

    def update(self, obj, validated_data):
        extras = validated_data.pop("extras")

        available_keys = obj.extras.keys()

        for key in extras:
                    obj.extras = {obj.extras, "key": extras[key]

        obj.save()
        obj.update(validated_data)
        return obj
'''

class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Picture
        fields = ['idx', 'image']