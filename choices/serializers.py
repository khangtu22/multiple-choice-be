from rest_framework import serializers

from .models import ChoiceModel


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChoiceModel
        fields = "__all__"