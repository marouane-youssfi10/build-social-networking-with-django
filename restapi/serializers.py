from rest_framework import serializers, status
from accounts.models import Account
from posting.models import PostProject, PostJobs, TagsProjects, TagsJobs
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

class TagsProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TagsProjects
        fields = ('tag',)

class PostingProjectSerializer(serializers.ModelSerializer):
    # skills_tags_projects = serializers.StringRelatedField(many=False)
    # skills_tags_projects = TagsProjectsSerializer(many=True)
    class Meta:
        model = PostProject
        fields = ('user', 'name_project', 'epic_coder', 'location', 'start_price', 'end_price', 'description_project',
                    'skills_tags_projects')

class PostingJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostJobs
        fields = ('user', 'name_jobs', 'type_work_job', 'epic_coder', 'location', 'price', 'description_job',
         'skills_tags_jobs')


class TagsJobsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TagsJobs
        fields = ('tag',)