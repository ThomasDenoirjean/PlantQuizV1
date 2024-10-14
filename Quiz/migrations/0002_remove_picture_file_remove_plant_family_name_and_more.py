# Generated by Django 5.0.4 on 2024-05-09 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='picture',
            name='file',
        ),
        migrations.RemoveField(
            model_name='plant',
            name='family_name',
        ),
        migrations.RemoveField(
            model_name='plant',
            name='occurence',
        ),
        migrations.AddField(
            model_name='picture',
            name='url',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
