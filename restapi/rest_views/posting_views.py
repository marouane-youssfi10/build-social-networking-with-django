from rest_framework import generics, serializers, status
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from restapi.serializers import PostingProjectSerializer
from posting.models import PostProject

class PostingProjectViewsets(viewsets.ModelViewSet):
    print('--- PostingProjectViewsets ---')
    serializer_class = PostingProjectSerializer
    queryset = PostProject.objects.all()
    permission_classes = (IsAuthenticated,)

class PostingProjectAPIView(APIView):
    print('--- PostingProjectAPIView ---')
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        print('--- get ---')
        print('request = ', request.user)
        print('pk = ', pk)
        projects = PostProject.objects.get(id=pk)
        serializer = PostingProjectSerializer(projects)

        return Response(serializer.data)

    def post(self, request, pk):
        print('--- post ---')
        print('request = ', request.user)
        print('pk = ', pk)
        return Response('success', status=status.HTTP_200_OK)