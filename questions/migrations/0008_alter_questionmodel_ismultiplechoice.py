# Generated by Django 4.1.7 on 2023-03-26 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0007_alter_questionmodel_ismultiplechoice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionmodel',
            name='isMultipleChoice',
            field=models.BooleanField(default=False),
        ),
    ]
