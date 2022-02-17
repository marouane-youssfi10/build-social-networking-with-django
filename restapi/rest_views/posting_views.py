from rest_framework import generics, serializers, status
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action
from posting.models import PostProject, PostJobs, TagsProjects, TagsJobs
from restapi.serializers import (
    PostingProjectSerializer,
    PostingJobSerializer,
    TagsProjectsSerializer,
    TagsJobsSerializer,
)

class PostingProjectViewsets(viewsets.ModelViewSet):
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
            return Response({'message': 'your project post is deleted successfully'})
        except:
            return Response({'message': 'this post does not exist'})

    @action(detail=False, methods=['GET'], url_path='hide_unhide_project/(?P<pk>[^/.]+)')
    def hide_unhide_project(self, request, pk=None, *args):
        print('--- hide_project ---')
        print('pk = ', pk)
        post_project = self.get_queryset(pk)
        if post_project.hide is False:
            print('True')
            post_project.hide = True
        else:
            print('False')
            post_project.hide = False
        post_project.save()
        return Response({'message': 'success', 'hide': post_project.hide}, status=status.HTTP_200_OK)

class PostingProjectAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    # get all post user project
    def get(self, request):
        print('--- get ---')
        projects = PostProject.objects.filter(user=request.user)
        serializer = PostingProjectSerializer(projects, many=True)
        return Response(serializer.data,  status=status.HTTP_200_OK)

    # add new post
    def post(self, request):
        print('--- post ---')
        data = request.data
        skills_tag_project = data['skills_tags_projects']
        ids_of_tag_project = []
        for tag in skills_tag_project:
            tag_project, created = TagsProjects.objects.get_or_create(tags_users_projects=request.user, tag=tag)
            ids_of_tag_project.append(tag_project.id)

        data['user'] = request.user.id
        data['skills_tags_projects'] = ids_of_tag_project
        project_form = PostingProjectSerializer(data=data)
        # print('project_form.is_valid() = ', project_form.is_valid())
        # print('project_form.errors = ', project_form.errors)
        if project_form.is_valid():
            project_form.save()
            return Response({
                "status": "post project created successfully",
                "data": project_form.data
            }, status=status.HTTP_201_CREATED)
        return Response({'error': 'Form is not valid'}, status=status.HTTP_400_BAD_REQUEST)

class PostingJobViewsets(viewsets.ModelViewSet):
    serializer_class = PostingJobSerializer
    queryset = PostJobs.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_queryset(self, pk=None):
        print('--- get_queryset ---')
        if pk is not None:
            return PostJobs.objects.get(id=pk)
        jobs = PostJobs.objects.all()
        return jobs

    def list(self, request, *args, **kwargs):
        print('--- list ---')
        jobs = self.get_queryset()
        serializer = PostingJobSerializer(jobs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None, *args, **kwargs):
        print('--- update ---')
        job = self.get_queryset(pk)
        data = request.data

        job.name_jobs = data['name_jobs']
        job.type_work_job = data['type_work_job']
        job.epic_coder = data['epic_coder']
        job.location = data['location']
        job.price = data['price']
        job.description_job = data['description_job']
        job.save()
        return Response({
            'message': 'your job post is updated successfully',
            'data': request.data
        }, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None, *args, **kwargs):
        print('--- destroy ---')
        try:
            post_job = PostJobs.objects.get(id=pk)
            post_job.delete()
            return Response({'message': 'your job post is deleted successfully'})
        except:
            return Response({'message': 'this post does not exist'})

    @action(detail=False, methods=['GET'], url_path='hide_unhide_job/(?P<pk>[^/.]+)')
    def hide_unhide_job(self, request, pk=None, *args):
        print('--- hide_job ---')
        print('pk = ', pk)
        post_job = self.get_queryset(pk)
        if post_job.hide is False:
            print('True')
            post_job.hide = True
        else:
            print('False')
            post_job.hide = False
        post_job.save()
        return Response({'message': 'success', 'hide': post_job.hide}, status=status.HTTP_200_OK)

class PostingJobAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    # get all post user project
    def get(self, request):
        print('--- get ---')
        jobs = PostJobs.objects.filter(user=request.user)
        serializer = PostingJobSerializer(jobs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        print('--- post ---')
        data = request.data
        skills_tag_job = data['skills_tags_jobs']
        ids_of_tag_job = []
        for tag in skills_tag_job:
            tag_job, created = TagsJobs.objects.get_or_create(tags_users_jobs=request.user, tag=tag)
            ids_of_tag_job.append(tag_job.id)

        data['user'] = request.user.id
        data['skills_tags_jobs'] = ids_of_tag_job
        job_form = PostingJobSerializer(data=data)
        # print('job_form.is_valid() = ', job_form.is_valid())
        # print('job_form.errors = ', job_form.errors)
        if job_form.is_valid():
            job_form.save()
            return Response({
                "status": "post job created successfully",
                "data": job_form.data
            }, status=status.HTTP_201_CREATED)
        return Response({'error': 'Form is not valid'}, status=status.HTTP_400_BAD_REQUEST)

class DeleteTagsProjectsViewsets(viewsets.ModelViewSet):
    serializer_class = TagsProjectsSerializer
    permission_classes = (IsAuthenticated,)

    def destroy(self, request, pk=None, *args, **kwargs):
        print('--- destroy ---')
        try:
            tag_project = TagsProjects.objects.get(id=pk)
            tag_project.delete()
            return Response({'message': 'your tag project is deleted successfully'})
        except:
            return Response({'message': 'this post is not exist'})

class DeleteTagsJobsViewsets(viewsets.ModelViewSet):
    serializer_class = TagsJobsSerializer
    permission_classes = (IsAuthenticated,)

    def destroy(self, request, pk=None, *args, **kwargs):
        print('--- destroy ---')
        try:
            tag_job = TagsJobs.objects.get(id=pk)
            tag_job.delete()
            return Response({'message': 'your tag job is deleted successfully'})
        except:
            return Response({'message': 'this tag is not exist'})