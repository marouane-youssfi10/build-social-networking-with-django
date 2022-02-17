from rest_framework import generics, serializers, status
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework_simplejwt.views import TokenObtainPairView
from restapi.serializers import PostingProjectSerializer, PostingJobSerializer, TagsProjectsSerializer, TagsJobsSerializer
from posting.models import PostProject, PostJobs, TagsProjects, TagsJobs

class PostingProjectViewsets(viewsets.ModelViewSet):
    print('--- PostingProjectViewsets ---')
    serializer_class = PostingProjectSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self, pk=None):
        print('--- get_queryset ---')
        if pk is not None:
            return PostProject.objects.get(id=pk)
        projects = PostProject.objects.all()
        return projects

    def list(self, request, *args, **kwargs):
        print('--- list ---')
        projects = self.get_queryset()
        serializer = PostingProjectSerializer(projects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None, *args, **kwargs):
        print('--- update ---')
        project = self.get_queryset(pk)
        data = request.data

        project.name_project = data['name_project']
        project.location = data['location']
        project.start_price = data['start_price']
        project.end_price = data['end_price']
        project.description_project = data['description_project']
        project.save()
        return Response({
            'message': 'your project post is updated successfully',
            'data': request.data
        }, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None, *args, **kwargs):
        print('--- destroy ---')
        try:
            post_project = PostProject.objects.get(id=pk)
            post_project.delete()
            return Response({'message': 'your project post is delete successfully'})
        except:
            return Response({'message': 'this post does not exist'})

class PostingProjectAPIView(APIView):
    print('--- PostingProjectAPIView ---')
    permission_classes = (IsAuthenticated,)

    # get all post user jobs
    def get(self, request):
        print('--- get ---')
        projects = PostProject.objects.filter(user=request.user)
        serializer = PostingProjectSerializer(projects, many=True)
        return Response(serializer.data,  status=status.HTTP_200_OK)

    # add new post
    def post(self, request):
        print('--- post ---')
        data = request.data
        skills = data['skills_tags_projects']
        ids = []
        for tag in skills:
            tag, created = TagsProjects.objects.get_or_create(tags_users_projects=request.user, tag=tag)
            ids.append(tag.id)

        data['user'] = request.user.id
        data['skills_tags_projects'] = ids
        project_form = PostingProjectSerializer(data=data)
        if project_form.is_valid():
            project_form.save()
            return Response({
                "status": "post project created successfully",
                "data": project_form.data
            }, status=status.HTTP_201_CREATED)
        return Response({'error': 'Form is not valid'}, status=status.HTTP_400_BAD_REQUEST)

class PostingJobViewsets(viewsets.ModelViewSet):
    print('--- PostingJobViewsets ---')
    serializer_class = PostingJobSerializer
    queryset = PostJobs.objects.all()
    permission_classes = (IsAuthenticated,)

