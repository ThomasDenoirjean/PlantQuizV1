# Generated by Django 5.0.4 on 2024-05-09 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0006_alter_plant_family_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='copyright',
            field=models.CharField(default=2, max_length=100),
            preserve_default=False,
        ),
    ]
