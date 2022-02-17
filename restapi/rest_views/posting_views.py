from rest_framework import generics, serializers, status
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action
from posting.models import PostProject, PostJobs, TagsProjects, TagsJobs
from comment.models import CommentProjects, CommentJobs
from accounts.models import UserProfile
from restapi.serializers import (
    PostingProjectSerializer,
    PostingJobSerializer,
    TagsProjectsSerializer,
    TagsJobsSerializer,

    # Comment
    CommentProjectSerializer,
    CommentJobSerializer
)

class PostingProjectViewsets(viewsets.ModelViewSet):
    serializer_class = PostingProjectSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self, pk=None):
        print('--- get_queryset ---')
        if pk is not None:
            try:
                return PostProject.objects.get(id=pk)
            except:
                # return Response({'message': 'this post is not exists'}, status=status.HTTP_400_BAD_REQUEST)
                raise serializers.ValidationError({'message': 'this post is not exists'})

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
    def hide_unhide_project(self, request, pk=None, *args, **kwargs):
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

    @action(detail=False, methods=['GET'], url_path='add_remove_like_project/(?P<pk>[^/.]+)')
    def add_remove_like_project(self, request, pk=None, *args, **kwargs):
        print('--- add_remove_like_project ---')
        post_project = self.get_queryset(pk)

        if not request.user in post_project.likes.all():
            post_project.likes.add(request.user)
        else:
            post_project.likes.remove(request.user)
        post_project.save()
        return Response({'message': 'success'}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['GET'], url_path='viewers_project/(?P<pk>[^/.]+)')
    def viewers_project(self, request, pk=None, *args, **kwargs):
        print('--- viewers_project ---')
        post_project = self.get_queryset(pk)
        post_project.viewers_project.add(request.user)
        post_project.save()
        return Response({'message': 'success'}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['GET'], url_path='saved_projects/(?P<pk>[^/.]+)')
    def saved_projects(self, request, pk=None, *args, **kwargs):
        post_project = self.get_queryset(pk)
        user_profile = UserProfile.objects.get(user=request.user)
        if not post_project in user_profile.my_bids_projects.all():
            user_profile.my_bids_projects.add(post_project.id)
            user_profile.save()
            return Response({'message': 'the post project saved successfully'}, status=status.HTTP_200_OK)
        return Response({'message': 'the project post already saved'}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['POST'], url_path='add_comment_project/(?P<pk>[^/.]+)')
    def add_comment_project(self, request, pk=None, *args, **kwargs):
        post_project = self.get_queryset(pk)
        data = request.data
        user = request.user
        try:
            comment_project = CommentProjects.objects.create(
                post_project=post_project,
                user_post=user,
                body=data['body']
            )
            comment_project.save()
            return Response({'message': 'Your Comment on project post is created Successfully'},
                            status=status.HTTP_201_CREATED)
        except:
            return Response({'message': 'form is not valid'}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['PUT'], url_path='update_comment_project/(?P<pk>[^/.]+)')
    def update_comment_project(self, request, pk=None, *args, **kwargs):
        data = request.data

        try:
            comment_project = CommentProjects.objects.get(id=pk)
            comment_project.body = data['body']
            comment_project.save()
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response({'message': 'Your Comment on project post is Updated Successfully'},
                        status=status.HTTP_201_CREATED)


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
    permission_classes = (IsAuthenticated,)

    def get_queryset(self, pk=None):
        print('--- get_queryset ---')
        if pk is not None:
            try:
                return PostJobs.objects.get(id=pk)
            except:
                raise serializers.ValidationError({'message': 'this post is not exists'})
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

    @action(detail=False, methods=['GET'], url_path='add_remove_like_job/(?P<pk>[^/.]+)')
    def add_remove_like_job(self, request, pk=None, *args):
        print('--- add_remove_like_job ---')
        post_job = self.get_queryset(pk)

        if not request.user in post_job.likes.all():
            post_job.likes.add(request.user)
        else:
            post_job.likes.remove(request.user)
        post_job.save()
        return Response({'message': 'success'}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['GET'], url_path='viewers_job/(?P<pk>[^/.]+)')
    def viewers_job(self, request, pk=None, *args, **kwargs):
        print('--- viewers_job ---')
        post_job = self.get_queryset(pk)
        post_job.viewers_job.add(request.user)
        post_job.save()
        return Response({'message': 'success'}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['GET'], url_path='saved_jobs/(?P<pk>[^/.]+)')
    def saved_jobs(self, request, pk=None, *args, **kwargs):
        post_job = self.get_queryset(pk)
        user_profile = UserProfile.objects.get(user=request.user)
        if not post_job in user_profile.saved_jobs.all():
            user_profile.saved_jobs.add(post_job.id)
            user_profile.save()
            return Response({'message': 'the post job saved successfully'}, status=status.HTTP_200_OK)
        return Response({'message': 'the job post already saved'}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['POST'], url_path='add_comment_job/(?P<pk>[^/.]+)')
    def add_comment_job(self, request, pk=None, *args, **kwargs):
        post_job = self.get_queryset(pk)
        data = request.data
        user = request.user
        try:
            comment_job = CommentJobs.objects.create(
                post_job=post_job,
                user_job=user,
                body=data['body']
            )
            comment_job.save()
            return Response({'message': 'Your Comment on job post is created Successfully'},
                            status=status.HTTP_201_CREATED)
        except:
            return Response({'message': 'form is not valid'}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['PUT'], url_path='update_comment_job/(?P<pk>[^/.]+)')
    def update_comment_job(self, request, pk=None, *args, **kwargs):
        data = request.data

        try:
            comment_job = CommentJobs.objects.get(id=pk)
            comment_job.body = data['body']
            comment_job.save()
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response({'message': 'Your Comment on job post is Updated Successfully'},
                        status=status.HTTP_201_CREATED)

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
