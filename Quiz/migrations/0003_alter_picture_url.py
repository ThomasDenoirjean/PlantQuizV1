# Generated by Django 5.0.4 on 2024-05-09 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0002_remove_picture_file_remove_plant_family_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='url',
            field=models.CharField(max_length=100),
        ),
    ]
