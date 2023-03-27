from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView

from choices.models import ChoiceModel
from choices.serializers import ChoiceSerializer
from questions.models import QuestionModel
from questions.serializers import QuestionSerializer

from random import choice

class ListQuestionAPIView(ListAPIView):
    """This endpoint list all of the available todos from the database"""
    queryset = QuestionModel.objects.all()
    serializer_class = QuestionSerializer

class CreateQuestionAPIView(CreateAPIView):
    """This endpoint allows for creation of a choice"""
    queryset = QuestionModel.objects.all()
    serializer_class = QuestionSerializer

class UpdateQuestionAPIView(UpdateAPIView):
    """This endpoint allows for updating a specific choice by passing in the id of the choice to update"""
    queryset = QuestionModel.objects.all()
    serializer_class = QuestionSerializer

class DeleteQuestionAPIView(DestroyAPIView):
    """This endpoint allows for deletion of a specific Question from the database"""
    queryset = QuestionModel.objects.all()
    serializer_class = QuestionSerializer


class GetChoiceByQuestionIDAPIView(ListAPIView):
    serializer_class = ChoiceSerializer

    def get_queryset(self):
        question_id = self.kwargs['question_id']
        return ChoiceModel.objects.filter(question=question_id)


class RandomQuestionAPIView(ListAPIView):
    serializer_class = QuestionSerializer

    def get_queryset(self):
        return QuestionModel.objects.first()


class GetQuestionAPIView(ListAPIView):
    serializer_class = QuestionSerializer

    def get_queryset(self):
        question_id = self.kwargs['question_id']
        queryset = QuestionModel.objects.filter(id=question_id)
        return queryset
