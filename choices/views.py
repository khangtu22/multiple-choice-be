from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
# Create your views here.

# Create your views here.
from choices.models import ChoiceModel
from choices.serializers import ChoiceSerializer


class ListChoiceAPIView(ListAPIView):
    """This endpoint list all of the available todos from the database"""
    queryset = ChoiceModel.objects.all()
    serializer_class = ChoiceSerializer

class CreateChoiceAPIView(CreateAPIView):
    """This endpoint allows for creation of a choice"""
    queryset = ChoiceModel.objects.all()
    serializer_class = ChoiceSerializer

class UpdateChoiceAPIView(UpdateAPIView):
    """This endpoint allows for updating a specific choice by passing in the id of the choice to update"""
    queryset = ChoiceModel.objects.all()
    serializer_class = ChoiceSerializer

class DeleteChoiceAPIView(DestroyAPIView):
    """This endpoint allows for deletion of a specific Choice from the database"""
    queryset = ChoiceModel.objects.all()
    serializer_class = ChoiceSerializer
