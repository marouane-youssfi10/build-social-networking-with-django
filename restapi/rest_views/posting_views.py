from rest_framework import generics, serializers, status
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from restapi.serializers import PostingProjectSerializer, PostingJobSerializer
from posting.models import PostProject, PostJobs

class PostingProjectViewsets(viewsets.ModelViewSet):
    print('--- PostingProjectViewsets ---')
    serializer_class = PostingProjectSerializer
    queryset = PostProject.objects.all()
    permission_classes = (IsAuthenticated,)

class PostingJobViewsets(viewsets.ModelViewSet):
    print('--- PostingJobViewsets ---')
    serializer_class = PostingJobSerializer
    queryset = PostJobs.objects.all()
    permission_classes = (IsAuthenticated,)

class PostingProjectAPIView(APIView):
    print('--- PostingProjectAPIView ---')
    permission_classes = (IsAuthenticated,)

    # get all post user jobs
    def get(self, request):
        print('--- get ---')
        print('request = ', request.user)
        projects = PostProject.objects.filter(user=request.user)
        serializer = PostingProjectSerializer(projects, many=True)
        return Response(serializer.data,  status=status.HTTP_200_OK)

    def post(self, request):
        print('--- post ---')
        data = request.data
        data['user'] = request.user.id
        project_form = PostingProjectSerializer(data=data)
        if project_form.is_valid():
            project_form.save()
            return Response({
                "status": "post project created successfully",
                "data": project_form.data
            }, status=status.HTTP_201_CREATED)
        return Response({'error': 'Form is not valid'}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        print('--- update ---')
        print('request.data = ', request.data)
        return Response({'message': 'ok'}, status=status.HTTP_200_OK)
