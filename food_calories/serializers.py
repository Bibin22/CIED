from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User



class FoodAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ['food_name', 'calorie']


class FoodListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ['food_id','food_name', 'calorie']


class LabelListSerializer(serializers.ModelSerializer):
    food = serializers.CharField(source='food_name.food_name')

    class Meta:
        model = Label
        fields = ['label_id','food', 'label']


class LabelAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Label
        fields = ['food_name', 'label']


class ActivityAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Activities
        fields = ['activity_name', 'calorie_burnout']


class ActivityListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Activities
        fields = ['activity_id','activity_name', 'calorie_burnout', 'is_approved']