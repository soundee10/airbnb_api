import email
from sre_constants import GROUPREF_EXISTS

from click import password_option
from pkg_resources import AvailableDistributions
from rest_framework import serializers
from .models import User


class RelatedUserSerialzer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "avatar",
            "superhost",
        )


class ReadUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = (
            "groups",
            "user_permissions",
            "password",
            "last_login",
            "is_superuser",
            "is_staff",
            "is_active",
            "date_joined",
        )