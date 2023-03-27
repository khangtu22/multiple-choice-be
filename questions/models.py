from django.db import models
import uuid

from banks.models import BankModel


class QuestionModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    question = models.CharField(max_length=255, blank=True)
    numOfChoice = models.IntegerField(default=0)
    isMultipleChoice = models.BooleanField(default=False)
    answer = models.CharField(max_length=255, blank=True)
    explain = models.CharField(max_length=255, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "questions"
        ordering = ['-createdAt']

        def __str__(self) -> str:
            return self.title
