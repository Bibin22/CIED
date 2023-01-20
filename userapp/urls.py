from django.urls import path
from .views import *

urlpatterns = [
    path('meal_add', MealAdd.as_view(), name='meal_add'),
    path('meal_edit/<str:id>',MealEdit.as_view(), name='meal_edit'),

    path('record_add', RecordAdd.as_view(), name='record_add'),
    path('new_activity_add', NewActivityAdd.as_view(), name='new_activity_add'),
    path('record_edit/<str:id>',RecordEdit.as_view(), name='record_edit'),



]