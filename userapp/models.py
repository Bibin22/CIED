from django.db import models
from food_calories.models import *
import uuid


class Meal(models.Model):
    meal_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    food_name = models.ForeignKey(Food, on_delete=models.CASCADE, null=True, blank=True)
    consumed = models.CharField(max_length=50, null=True, blank=True)


    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return str(self.food_name)


class ActivityRecord(models.Model):
    activity_rec_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    activity = models.ForeignKey(Activities, on_delete=models.CASCADE, null=True, blank=True)
    time = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return str(self.activity)




class NewActivity(models.Model):
    new_activity_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    activity_name = models.CharField(max_length=50, null=True, blank=True)
    calorie_burnout = models.CharField(max_length=50, null=True, blank=True)
    is_approved = models.BooleanField(default=True)



    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return str(self.activity_name)
