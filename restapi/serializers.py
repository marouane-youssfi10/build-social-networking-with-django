from accounts.models import Account
from posting.models import PostProject, PostJobs, TagsProjects, TagsJobs
from comment.models import CommentProjects, CommentJobs

from rest_framework import serializers, status
from rest_framework.response import Response

class RegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=50, min_length=6)
    username = serializers.CharField(max_length=50, min_length=6)
    password = serializers.CharField(max_length=150, write_only=True)

    class Meta:
        model = Account
        fields = ('id', 'first_name', 'last_name', 'email', 'username', 'password')

    def validate(self, args):
        print('--- validate ---')
        email = args.get('email', None)
        password = args.get('password', None)
        confirm_password = args.get('confirm_password', None)

        if Account.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email': ('email already exists')})

        return super().validate(args)

    def create(self, validate_data):
        return Account.objects.create_user(**validate_data)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('id', 'username')


# --------------------- Comment section ---------------------------------
class CommentProjectSerializer(serializers.ModelSerializer):
    # post_project = serializers.StringRelatedField(many=False)
    user_post = serializers.StringRelatedField(many=False)
    class Meta:
        model = CommentProjects
        fields = ('user_post', 'body')

class CommentJobSerializer(serializers.ModelSerializer):
    # post_job = serializers.StringRelatedField(many=False)
    user_job = serializers.StringRelatedField(many=False)
    class Meta:
        model = CommentJobs
        fields = ('user_job', 'body')

# ----------------------- Post section -----------------------------
class TagsProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TagsProjects
        fields = ('tag',)

class TagsJobsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TagsJobs
        fields = ('tag',)

class PostingProjectSerializer(serializers.ModelSerializer):
    likes = UserSerializer(many=True)
    viewers_project = UserSerializer(many=True)
    skills_tags_projects = TagsProjectsSerializer(many=True)
    # comment_project = CommentProjectSerializer(many=True, read_only=True)
    class Meta:
        model = PostProject
        fields = ('id', 'user', 'name_project', 'epic_coder', 'location', 'start_price', 'end_price', 'description_project',
                    'skills_tags_projects', 'likes', 'viewers_project')

class PostingJobSerializer(serializers.ModelSerializer):
    likes = UserSerializer(many=True)
    viewers_job = UserSerializer(many=True)
    skills_tags_jobs = TagsJobsSerializer(many=True)
    class Meta:
        model = PostJobs
        fields = ('user', 'name_jobs', 'type_work_job', 'epic_coder', 'location', 'price', 'description_job',
         'skills_tags_jobs', 'likes', 'viewers_job')

