# Generated by Django 4.1.7 on 2023-03-26 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_questionmodel_bank'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questionmodel',
            name='category',
        ),
        migrations.RemoveField(
            model_name='questionmodel',
            name='content',
        ),
        migrations.RemoveField(
            model_name='questionmodel',
            name='title',
        ),
        migrations.AddField(
            model_name='questionmodel',
            name='answer',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='questionmodel',
            name='explain',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='questionmodel',
            name='isMultipleChoice',
            field=models.BooleanField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='questionmodel',
            name='numOfChoice',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='questionmodel',
            name='question',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
