from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User



class MealAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ['food_name', 'consumed']


class MealListSerializer(serializers.ModelSerializer):
    food = serializers.CharField(source='food_name.food_name')
    class Meta:
        model = Meal
        fields = ['meal_id','food', 'consumed']


class RecordListSerializer(serializers.ModelSerializer):
    activity_name = serializers.CharField(source='activity.activity_name')

    class Meta:
        model = ActivityRecord
        fields = ['activity_rec_id','activity_name', 'time']


class RecordAddSerializer(serializers.ModelSerializer):

    class Meta:
        model = ActivityRecord
        fields = ['activity', 'time']


