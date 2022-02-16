from .serializers import RegistrationSerializer
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class RegistrationNewUserAPI(generics.GenericAPIView):
    serializer_class = RegistrationSerializer

    def post(self, request, *args, **kwargs):
        try:
            user = self.get_serializer(data=request.data)
            if user.is_valid():
                user.save()
                return Response({
                    'message': 'User created successfully',
                    "user": user.data
                }, status=status.HTTP_201_CREATED)

            return Response(user.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'message': f'{e}'}, status=status.HTTP_403_FORBIDDEN)

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['username'] = user.username
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name
        token['email'] = user.email

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer