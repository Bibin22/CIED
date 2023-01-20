from django.db import models
import uuid


class Food(models.Model):
    food_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    food_name = models.CharField(max_length=50, null=True, blank=True)
    calorie = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return str(self.food_name)


class Label(models.Model):
    label_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    food_name = models.ForeignKey(Food, on_delete=models.CASCADE, null=True, blank=True)
    label= models.CharField(max_length=50, null=True, blank=True)


    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return str(self.label)


class Activities(models.Model):
    activity_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    activity_name = models.CharField(max_length=50, null=True, blank=True)
    calorie_burnout = models.CharField(max_length=50, null=True, blank=True)
    is_approved = models.BooleanField(default=False)


    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return str(self.activity_name)