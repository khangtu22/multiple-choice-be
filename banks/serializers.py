from rest_framework import serializers
from rest_framework.fields import FileField

from .models import BankModel


class BankSerializer(serializers.ModelSerializer):
    file_url = FileField()

    class Meta:
        model = BankModel
        fields = "__all__"