from django.contrib.auth.models import User
from rest_framework import serializers

class UsersSerializer(serializers.ModelSerializer):
   class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password', 'email']

        def validate_password(self, value):
            if len(value) < 8:
                raise serializers.ValidationError("Password must be at least 8 characters long")
            return value
        
        def validate_username(self, value):
            if User.objects.filter(username=value).exists():
                raise serializers.ValidationError("Username already exists")
            return value

        def create(self, validated_data):
            user = User.objects.create_user(**validated_data)
            return user