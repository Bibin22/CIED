from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import *


#user creation
class UserRegistration(APIView):
    serializer_class = UserRegisterSerializer
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        print(request.user.is_superuser, 'mmmm')
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = "Registrations Sucessfull"
            data['username'] = account.username
            data['email'] = account.email
            data['token'] = Token.objects.get(user=account).key
        else:
            data = serializer.errors
        return Response(data, status=status.HTTP_201_CREATED)


#logout

class LogOut(APIView):
    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)