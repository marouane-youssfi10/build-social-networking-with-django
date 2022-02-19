from rest_framework import serializers, status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action
from notifications.models import NotificationProjects
from restapi.serializers import NotificationsSerializer


class NotificationsViewsets(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self, pk=None):
        print('--- get_queryset ---')
        if pk is not None:
            try:
                notification = NotificationProjects.objects.get(id=pk)
                return notification
            except:
                raise serializers.ValidationError({'message': 'this notification is not exists'})
        else:
            raise serializers.ValidationError({'message': 'you have to pass an id of notification user'})

    @action(detail=False, methods=['GET'], url_path='is_seen/(?P<pk>[^/.]+)')
    def is_seen(self, request, pk=None, *args, **kwargs):
        print('--- is_seen ---')
        notification = self.get_queryset(pk)
        notification.is_seen = True
        notification.save()
        return Response({'message': 'success', 'is_seen': notification.is_seen}, status=status.HTTP_200_OK)

class NotificationsAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    # get user notifications
    def get(self, request):
        print('--- get ---')
        notifications = NotificationProjects.objects.filter(to_user=request.user)
        serializer = NotificationsSerializer(notifications, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
