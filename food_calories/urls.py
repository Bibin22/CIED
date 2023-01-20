from django.urls import path
from .views import *

urlpatterns = [
    path('food_add', FoodAdd.as_view(), name='food_add'),
    path('food_edit/<str:id>',FoodEdit.as_view(), name='food_edit'),

    path('label_add', LabelAdd.as_view(), name='label_add'),
    path('label_edit/<str:id>', LabelEdit.as_view(), name='label_edit'),

    path('activity_add', ActivityAdd.as_view(), name='activity_add'),
    path('activity_edit/<str:id>', ActivityEdit.as_view(), name='activity_edit'),

]