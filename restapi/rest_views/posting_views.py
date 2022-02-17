from rest_framework import generics, serializers, status
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from restapi.serializers import PostingProjectSerializer, PostingJobSerializer, TagsProjectsSerializer, TagsJobsSerializer
from posting.models import PostProject, PostJobs, TagsProjects, TagsJobs

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

    # add new post
    def post(self, request):
        print('--- post ---')
        data = request.data
        # -------------------------------------
        skills = data['skills_tags_projects']
        print('skills = ', skills)
        ids = []
        for i in skills:
            tag, created = TagsProjects.objects.get_or_create(tags_users_projects=request.user, tag=i)
            print('tag = ', tag, '| created = ', created)
            ids.append(tag.id)
        print('ids = ', ids)
        # -------------------------------------
        data['user'] = request.user.id
        data['skills_tags_projects'] = ids
        project_form = PostingProjectSerializer(data=data)
        # print('project_form = ', project_form.is_valid())
        # print('tags_project_form = ', tags_project_form.is_valid())
        # print('project_form.errors = ', project_form.errors)
        # print('-----------------------------')
        if project_form.is_valid():
            # print('project_form["tag"]', project_form['tag'])
            # print('project_form["tag"]', project_form['skills_tags_projects'])
            project_form.save()
            # tags_project_form.save()
            return Response({
                "status": "post project created successfully",
                "data": project_form.data
            }, status=status.HTTP_201_CREATED)
        return Response({'error': 'Form is not valid'}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        print('--- update ---')
        print('request.data = ', request.data)
        return Response({'message': 'ok'}, status=status.HTTP_200_OK)

