from djoser.serializers import UserCreateSerializer, UserSerializer
from .models import User
from django.urls import reverse
from django.core.signing import Signer
from django.conf import settings

class CustomUserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'username', 'password', 'email', 'role')

    def create(self, validated_data):
        user = super().create(validated_data)

        if user.role == 'CLIENT':
            signer = Signer()
            encrypted_url = signer.sign(f"{user.username}-{user.id}")
            user.encrypted_url = encrypted_url  # Optional if you want to save it
            user.save()
            self.encrypted_url = encrypted_url  # Store it in serializer

        return user

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if hasattr(self, 'encrypted_url'):
            data['encrypted_url'] = self.encrypted_url
        return data

class CustomUserSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        model = User
        fields = ('id', 'username', 'email', 'role')
 
from rest_framework import serializers
from .models import UploadedFile

class FileUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedFile
        fields = ['id', 'file', 'uploaded_at']

    def validate_file(self, value):
        allowed_types = ['.pptx', '.docx', '.xlsx']
        if not any(str(value).endswith(ext) for ext in allowed_types):
            raise serializers.ValidationError("Only .pptx, .docx, .xlsx files are allowed.")
        return value
