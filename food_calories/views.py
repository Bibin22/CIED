from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import *



class FoodAdd(APIView):
    permission_classes = [IsAuthenticated]
    serializers_class = FoodAddSerializer

    def get(self, request):
        try:
            foods = Food.objects.all()
            serializer = FoodListSerializer(foods, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            result = {
                "msg": "something went wrong"
            }
            return Response(result, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        try:
            if request.user.is_superuser:
                serializer = FoodAddSerializer(data=request.data)
                print(request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(request.data, status=status.HTTP_201_CREATED)
                else:
                    data = serializer.errors
                    return Response(data, status=status.HTTP_400_BAD_REQUEST)
            else:
                results = {
                    "msg": "only admin can add foods "
                }
                return Response(results, status=status.HTTP_401_UNAUTHORIZED)
        except:
            results = {
                "msg": "something went wrong"
            }
            return Response(results, status=status.HTTP_400_BAD_REQUEST)


class FoodEdit(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = FoodAddSerializer

    def get(self, request, id):
        try:
            if request.user.is_superuser:
                food = Food.objects.get(food_id=id)
                serializer = FoodAddSerializer(food)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                results = {
                    "msg":"only admin can edit food details"
                }
                return Response(results, status=status.HTTP_401_UNAUTHORIZED)
        except:
            results = {
                "msg": "something went wrong"
            }
            return Response(results, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id):
        try:
            if request.user.is_superuser:
                food = Food.objects.get(food_id=id)
                serializer = FoodAddSerializer(food, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                else:
                    data = serializer.errors
                    return Response(data, status=status.HTTP_400_BAD_REQUEST)
            else:
                results = {
                    "msg": "only admin can edit food details"
                }
                return Response(results, status=status.HTTP_401_UNAUTHORIZED)

        except:
            results = {
                "msg": "something went wrong"
            }
            return Response(results, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            if request.user.is_superuser:
                Food.objects.get(food_id=id).delete()
                result = {
                    "msg":"Food Item deleted"
                }
                return Response(result, status=status.HTTP_204_NO_CONTENT)
            else:
                results = {
                    "msg": "only admin can edit food details"
                }
                return Response(results, status=status.HTTP_401_UNAUTHORIZED)
        except:
            results = {
                "msg": "something went wrong"
            }
            return Response(results, status=status.HTTP_400_BAD_REQUEST)



class LabelAdd(APIView):
    permission_classes = [IsAuthenticated]
    serializers_class = LabelAddSerializer

    def get(self, request):
        try:
            labels = Label.objects.all()
            serializer = LabelListSerializer(labels, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            result = {
                "msg": "something went wrong"
            }
            return Response(result, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        try:
            if request.user.is_superuser:
                serializer = LabelAddSerializer(data=request.data)
                print(request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(request.data, status=status.HTTP_201_CREATED)
                else:
                    data = serializer.errors
                    return Response(data, status=status.HTTP_400_BAD_REQUEST)
            else:
                results = {
                    "msg": "only admin can add labels "
                }
                return Response(results, status=status.HTTP_401_UNAUTHORIZED)
        except:
            results = {
                "msg": "something went wrong"
            }
            return Response(results, status=status.HTTP_400_BAD_REQUEST)


class LabelEdit(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = LabelAddSerializer

    def get(self, request, id):
        try:
            if request.user.is_superuser:
                label = Label.objects.get(label_id=id)
                serializer = LabelListSerializer(label)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                results = {
                    "msg":"only admin can edit Label details"
                }
                return Response(results, status=status.HTTP_401_UNAUTHORIZED)
        except:
            results = {
                "msg": "something went wrong"
            }
            return Response(results, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id):
        try:
            if request.user.is_superuser:
                food = Label.objects.get(label_id=id)
                serializer = LabelAddSerializer(food, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                else:
                    data = serializer.errors
                    return Response(data, status=status.HTTP_400_BAD_REQUEST)
            else:
                results = {
                    "msg": "only admin can edit Label details"
                }
                return Response(results, status=status.HTTP_401_UNAUTHORIZED)

        except:
            results = {
                "msg": "something went wrong"
            }
            return Response(results, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            if request.user.is_superuser:
                Label.objects.get(label_id=id).delete()
                result = {
                    "msg":"Label Item deleted"
                }
                return Response(result, status=status.HTTP_204_NO_CONTENT)
            else:
                results = {
                    "msg": "only admin can edit Label details"
                }
                return Response(results, status=status.HTTP_401_UNAUTHORIZED)
        except:
            results = {
                "msg": "something went wrong"
            }
            return Response(results, status=status.HTTP_400_BAD_REQUEST)


class ActivityAdd(APIView):
    permission_classes = [IsAuthenticated]
    serializers_class = ActivityAddSerializer

    def get(self, request):
        try:
            activities = Activities.objects.all()
            serializer = ActivityListSerializer(activities, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            result = {
                "msg": "something went wrong"
            }
            return Response(result, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        try:
            if request.user.is_superuser:
                serializer = ActivityAddSerializer(data=request.data)
                print(request.data)
                if serializer.is_valid():
                    serializer.validated_data['is_approved'] = True
                    serializer.save()
                    return Response(request.data, status=status.HTTP_201_CREATED)
                else:
                    data = serializer.errors
                    return Response(data, status=status.HTTP_400_BAD_REQUEST)
            else:
                results = {
                    "msg": "only admin can add activities "
                }
                return Response(results, status=status.HTTP_401_UNAUTHORIZED)
        except:
            results = {
                "msg": "something went wrong"
            }
            return Response(results, status=status.HTTP_400_BAD_REQUEST)


class ActivityEdit(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ActivityAddSerializer

    def get(self, request, id):
        try:
            if request.user.is_superuser:
                activities = Activities.objects.get(activity_id=id)
                serializer = ActivityAddSerializer(activities)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                results = {
                    "msg":"only admin can edit activity details"
                }
                return Response(results, status=status.HTTP_401_UNAUTHORIZED)
        except:
            results = {
                "msg": "something went wrong"
            }
            return Response(results, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id):
        try:
            if request.user.is_superuser:
                activities = Activities.objects.get(activity_id=id)
                serializer = ActivityAddSerializer(activities, data=request.data)
                if serializer.is_valid():
                    serializer.validated_data['is_approved'] = True
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                else:
                    data = serializer.errors
                    return Response(data, status=status.HTTP_400_BAD_REQUEST)
            else:
                results = {
                    "msg": "only admin can edit activity details"
                }
                return Response(results, status=status.HTTP_401_UNAUTHORIZED)

        except:
            results = {
                "msg": "something went wrong"
            }
            return Response(results, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            if request.user.is_superuser:
                Activities.objects.get(activity_id=id).delete()
                result = {
                    "msg":"Activity Item deleted"
                }
                return Response(result, status=status.HTTP_204_NO_CONTENT)
            else:
                results = {
                    "msg": "only admin can edit food details"
                }
                return Response(results, status=status.HTTP_401_UNAUTHORIZED)
        except:
            results = {
                "msg": "something went wrong"
            }
            return Response(results, status=status.HTTP_400_BAD_REQUEST)