from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from food_calories.serializers import *
from food_calories.models import *



class MealAdd(APIView):
    permission_classes = [IsAuthenticated]
    serializers_class = MealAddSerializer

    def get(self, request):
        try:
            meal = Meal.objects.all()
            serializer = MealListSerializer(meal, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            result = {
                "msg": "something went wrong"
            }
            return Response(result, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        try:

            serializer = MealAddSerializer(data=request.data)
            print(request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(request.data, status=status.HTTP_201_CREATED)
            else:
                data = serializer.errors
                return Response(data, status=status.HTTP_400_BAD_REQUEST)


        except:
            results = {
                "msg": "something went wrong"
            }
            return Response(results, status=status.HTTP_400_BAD_REQUEST)


class MealEdit(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = MealAddSerializer

    def get(self, request, id):
        try:

            meal = Meal.objects.get(meal_id=id)
            serializer = MealAddSerializer(meal)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except:
            results = {
                "msg": "something went wrong"
            }
            return Response(results, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id):
        try:

            meal = Meal.objects.get(meal_id=id)
            serializer = MealAddSerializer(meal, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                data = serializer.errors
                return Response(data, status=status.HTTP_400_BAD_REQUEST)


        except:
            results = {
                "msg": "something went wrong"
            }
            return Response(results, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:

            Meal.objects.get(meal_id=id).delete()
            result = {
                "msg":"Meal Item deleted"
            }
            return Response(result, status=status.HTTP_204_NO_CONTENT)

        except:
            results = {
                "msg": "something went wrong"
            }
            return Response(results, status=status.HTTP_400_BAD_REQUEST)


class RecordAdd(APIView):
    permission_classes = [IsAuthenticated]
    serializers_class = RecordAddSerializer

    def get(self, request):
        try:
            record = ActivityRecord.objects.all()
            serializer = RecordListSerializer(record, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            result = {
                "msg": "something went wrong"
            }
            return Response(result, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        try:

            serializer = RecordAddSerializer(data=request.data)
            print(request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(request.data, status=status.HTTP_201_CREATED)
            else:
                data = serializer.errors
                return Response(data, status=status.HTTP_400_BAD_REQUEST)


        except:
            results = {
                "msg": "something went wrong"
            }
            return Response(results, status=status.HTTP_400_BAD_REQUEST)


class RecordEdit(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = RecordAddSerializer

    def get(self, request, id):
        try:

            record = ActivityRecord.objects.get(activity_rec_id=id)
            serializer = RecordAddSerializer(record)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except:
            results = {
                "msg": "something went wrong"
            }
            return Response(results, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id):
        try:

            record = ActivityRecord.objects.get(activity_rec_id=id)
            serializer = RecordAddSerializer(record, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                data = serializer.errors
                return Response(data, status=status.HTTP_400_BAD_REQUEST)


        except:
            results = {
                "msg": "something went wrong"
            }
            return Response(results, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:

            ActivityRecord.objects.get(activity_rec_id=id).delete()
            result = {
                "msg": "Activity Record Item deleted"
            }
            return Response(result, status=status.HTTP_204_NO_CONTENT)

        except:
            results = {
                "msg": "something went wrong"
            }
            return Response(results, status=status.HTTP_400_BAD_REQUEST)



class NewActivityAdd(APIView):
    permission_classes = [IsAuthenticated]
    serializers_class = ActivityAddSerializer

    def get(self, request):

        activities = Activities.objects.all()
        serializer = ActivityListSerializer(activities, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self, request):


        serializer = ActivityAddSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():

            serializer.save()
            return Response(request.data, status=status.HTTP_201_CREATED)
        else:
            data = serializer.errors
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

