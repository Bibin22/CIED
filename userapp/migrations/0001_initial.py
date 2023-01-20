# Generated by Django 4.1.5 on 2023-01-19 23:52

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('food_calories', '0002_rename_activitie_id_activities_activity_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewActivity',
            fields=[
                ('new_activity_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('activity_name', models.CharField(blank=True, max_length=50, null=True)),
                ('calorie_burnout', models.CharField(blank=True, max_length=50, null=True)),
                ('is_approved', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('meal_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('consumed', models.CharField(blank=True, max_length=50, null=True)),
                ('food_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='food_calories.food')),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='ActivityRecord',
            fields=[
                ('activity_rec_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('time', models.TimeField(blank=True, null=True)),
                ('activity', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='food_calories.activities')),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
    ]