from accounts.models import Account, UserProfile
from posting.models import PostProject, PostJobs, TagsProjects, TagsJobs
from comment.models import CommentProjects, CommentJobs
from follow.models import Follow
from notifications.models import NotificationProjects
from conversations.models import Message
from user_profile.models import Experience_user, Social_media, TagsUser

from rest_framework import serializers, status
from rest_framework.response import Response


# --------------------- Authentications section ---------------------------------
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


# ----------------------- User Profile section -------------------------

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id', 'user', 'title', 'overview', 'education_title', 'education_year_start',
                  'education_year_end', 'education_description', 'location_country', 'location_city',
                  'skills_tags_user', 'links_media', 'experience', 'likes', 'saved_jobs', 'my_bids_projects', 'viewers')

# ----------------------- User Experience section --------------------------

class UserExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience_user
        fields = ('id', 'experience_user', 'experince_title', 'experince_description')

# ----------------------- Social Media section --------------------------

class SocialMediaLinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Social_media
        fields = ('id', 'social_media_user', 'name', 'link')

# ----------------------- Social Media section --------------------------

class TagsUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TagsUser
        fields = ('id', 'tags_user', 'tag')

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

# ----------------------- Follow section -----------------------------
class FollowSerializer(serializers.ModelSerializer):
    following = serializers.StringRelatedField(many=True)
    followers = serializers.StringRelatedField(many=True)
    class Meta:
        model = Follow
        fields = ('id', 'user', 'following', 'followers')


# ----------------------- Notifications section -----------------------------

class NotificationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationProjects
        fields = ('id', 'post_job', 'post_project', 'sender', 'to_user', 'notification_type', 'body', 'is_seen')

# ----------------------- conversation section -----------------------------

class ConversationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('id', 'user', 'sender', 'recipient', 'body', 'is_read', 'created', 'updated')
