from rest_framework import serializers, status
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action
from follow.models import Follow
from restapi.serializers import FollowSerializer
from rest_framework.decorators import api_view, permission_classes


class FollowViewsets(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self, pk=None):
        print('--- get_queryset ---')
        if pk is not None:
            try:
                return Follow.objects.get(id=pk)
            except:
                raise serializers.ValidationError({'message': 'this user is not exists'})

    @action(detail=False, methods=['GET'], url_path='follow_unfollow/(?P<pk>[^/.]+)')
    def follow_unfollow(self, request, pk=None, *args, **kwargs):
        print('--- follow_unfollow ---')
        print('pk = ', pk)
        my_profile_follow = Follow.objects.get(user=request.user)
        obj = self.get_queryset(pk)
        if not obj.user in my_profile_follow.following.all():
            my_profile_follow.following.add(obj.user)
            obj.followers.add(my_profile_follow.user)
            return Response({'message': 'follow'}, status=status.HTTP_200_OK)
        else:
            my_profile_follow.following.remove(obj.user)
            obj.followers.remove(my_profile_follow.user)
            return Response({'message': 'unfollow'}, status=status.HTTP_200_OK)

class FollowAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    # get user follow
    def get(self, request):
        print('--- get ---')
        follow = Follow.objects.filter(user=request.user)
        serializer = FollowSerializer(follow, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_user_follow(request, pk):
    print('--- get_user_follow ---')
    try:
        follow = Follow.objects.get(id=pk)
        serializer = FollowSerializer(follow, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except:
        return Response({'message': 'not exists'}, status=status.HTTP_400_BAD_REQUEST)