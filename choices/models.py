from django.db import models
import uuid

from questions.models import QuestionModel


class ChoiceModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    question = models.ForeignKey(QuestionModel, on_delete=models.CASCADE)
    content = models.CharField(max_length=255)
    isRightChoice = models.BooleanField(default=False)

    class Meta:
        db_table = "choices"