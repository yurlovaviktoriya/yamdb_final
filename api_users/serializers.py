from rest_framework import serializers

from api_users.models import CustomUser


class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('email',)
        model = CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'first_name',
            'last_name',
            'username',
            'bio',
            'email',
            'role'
        )
        model = CustomUser
