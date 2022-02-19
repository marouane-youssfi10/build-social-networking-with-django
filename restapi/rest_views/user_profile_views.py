from rest_framework import serializers, status
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action, api_view, permission_classes
from accounts.models import UserProfile, Account, TagsUser, Social_media, Experience_user
from restapi.serializers import UserProfileSerializer, UserExperienceSerializer, SocialMediaLinksSerializer, TagsUserSerializer


class UserProfileViewsets(viewsets.ModelViewSet):
    # serializer_class = PostingProjectSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self, pk=None):
        print('--- get_queryset ---')
        if pk is not None:
            try:
                user_profile = UserProfile.objects.get(id=pk)
                return user_profile
            except:
                raise serializers.ValidationError({'message': 'this user profile is not exists'})

        return UserProfile.objects.all()

    def create(self, request, *args, **kwargs):
        print('--- create skills user---')
        data = request.data

        if data['tag'] == '' or data['tag'] is None:
            return Response({'message': 'there is no value of tag'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            tag_user = TagsUser.objects.create(tags_user=request.user, tag=data['tag'])
            tag_user.save()
            return Response({'message': 'your tag is created successfully'})
        except:
            return Response({'message': 'this user is not exists'})

    def update(self, request, pk=None, *args, **kwargs):
        print('--- update ---')
        user_profile = self.get_queryset(pk)
        data = request.data

        try:
            user_profile.title = data.get('title', user_profile.title)
            user_profile.overview = data.get('overview', user_profile.overview)
            user_profile.education_title = data.get('education_title', user_profile.education_title)
            user_profile.education_year_start = data.get('education_year_start', user_profile.education_year_start)
            user_profile.education_year_end = data.get('education_year_end', user_profile.education_year_end)
            user_profile.education_description = data.get('education_description', user_profile.education_description)
            user_profile.location_country = data.get('location_country', user_profile.location_country)
            user_profile.location_city = data.get('location_city', user_profile.location_city)
            user_profile.save()
        except Exception as err:
            return Response({'message': 'Form is not valid', 'error': f'{err}'}, status=status.HTTP_400_BAD_REQUEST)

        return Response({
            'message': 'your user profile is updated successfully',
            'data': data
        }, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None, *args, **kwargs):
        print('--- destroy skills user---')
        try:
            tag_user = TagsUser.objects.get(id=pk)
            tag_user.delete()
            return Response({'message': 'your tag is deleted successfully'})
        except:
            return Response({'message': 'this tag does not exist'}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['PUT'], url_path='update_experience_user/(?P<pk>[^/.]+)')
    def update_experience_user(self, request, pk=None, *args):
        user_experience = Experience_user.objects.get(id=pk)
        data = request.data
        try:
            user_experience.experince_title = data.get('experince_title', user_experience.experince_title)
            user_experience.experince_description = data.get('experince_description', user_experience.experince_description)
            user_experience.save()
        except Exception as err:
            return Response({'message': 'Form is not valid', 'error': f'{err}'}, status=status.HTTP_400_BAD_REQUEST)

        return Response({
            'message': 'your Experience is updated successfully',
            'data': data
        }, status=status.HTTP_200_OK)

    @action(detail=False, methods=['PUT'], url_path='update_link_social_media/(?P<pk>[^/.]+)')
    def update_link_social_media(self, request, pk=None, *args):
        link_social_media = Social_media.objects.get(id=pk)
        data = request.data
        try:
            link_social_media.name = data.get('name', link_social_media.name)
            link_social_media.link = data.get('link', link_social_media.link)
            link_social_media.save()
        except Exception as err:
            return Response({'message': 'Form is not valid', 'error': f'{err}'}, status=status.HTTP_400_BAD_REQUEST)

        return Response({
            'message': 'your links is updated successfully',
            'data': data
        }, status=status.HTTP_200_OK)

    @action(detail=False, methods=['GET'])
    def get_user_experience(self, request, *args):
        print('--- get_user_experience ---')
        try:
            experience_user = Experience_user.objects.filter(experience_user=request.user)
            serializer = UserExperienceSerializer(experience_user, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as err:
            return Response({'message': 'this user does not exists', 'error': f'{err}'}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['GET'])
    def get_user_links(self, request, *args):
        print('--- get_user_links ---')
        try:
            tags_user = Social_media.objects.filter(social_media_user=request.user)
            serializer = SocialMediaLinksSerializer(tags_user, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({'message': 'this user does not exists'}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['GET'])
    def get_user_skills_tags(self, request, *args):
        print('--- get_user_links ---')
        try:
            tags_user = TagsUser.objects.filter(tags_user=request.user)
            serializer = TagsUserSerializer(tags_user, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({'message': 'this user does not exists'}, status=status.HTTP_400_BAD_REQUEST)

class UserProfileAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    # get user profile
    def get(self, request):
        print('--- get ---')
        user_profile = UserProfile.objects.filter(user=request.user)
        serializer = UserProfileSerializer(user_profile, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)