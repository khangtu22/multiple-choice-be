from django.db import models
import uuid


def upload_to(instance, filename):
    return 'file-banks/{filename}'.format(filename=filename)


class BankModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255, unique=True)
    content = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    file_url = models.FileField(upload_to=upload_to, blank=True, null=True)

    class Meta:
        db_table = "banks"
        ordering = ['-createdAt']

        def __str__(self) -> str:
            return self.title
