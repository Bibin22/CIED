# Generated by Django 4.1.5 on 2023-01-20 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_calories', '0003_activities_is_approved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activities',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
    ]
