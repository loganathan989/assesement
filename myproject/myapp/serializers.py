from rest_framework import serializers # type: ignore

from .models import *




class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = "__all__"