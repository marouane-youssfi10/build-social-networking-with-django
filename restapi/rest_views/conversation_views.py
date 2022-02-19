from rest_framework import serializers, status
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action
from conversations.models import Message
from accounts.models import Account
from restapi.serializers import ConversationSerializer
from rest_framework.decorators import api_view, permission_classes

class ConversationViewsets(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self, pk=None):
        print('--- get_queryset ---')
        if pk is not None:
            try:
                return Account.objects.get(id=pk)
            except:
                raise serializers.ValidationError({'message': 'this user is not exists'})
        else:
            raise serializers.ValidationError({'message': 'you have to pass an id of user'})

    def list(self, request, *args, **kwargs):
        print('--- list ---')
        follow = self.get_queryset()
        serializer = ConversationSerializer(follow, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['GET'], url_path='get_messages/(?P<pk>[^/.]+)')
    def get_messages(self, request, pk=None, *args, **kwargs):
        recipient = self.get_queryset(pk)
        messages = Message.objects.filter(user=request.user, sender=request.user, recipient=recipient) | Message.objects.filter(user=request.user, sender=recipient, recipient=request.user)
        serializer = ConversationSerializer(messages, many=True)
        return Response({'messages': serializer.data}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['GET'], url_path='add_new_user_to_my_conversations/(?P<pk>[^/.]+)')
    def add_new_user_to_my_conversations(self, request, pk=None, *args, **kwargs):
        to_user = self.get_queryset(pk)
        Message.objects.create(user=request.user, sender=request.user, recipient=to_user)
        Message.objects.create(user=to_user, sender=request.user, recipient=to_user)

        return Response({'messages': 'user added successfully'}, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['POST'], url_path='send_message/(?P<pk>[^/.]+)')
    def send_message(self, request, pk=None, *args, **kwargs):
        to_user = self.get_queryset(pk)
        data = request.data
        try:
            Message.objects.create(user=request.user, sender=request.user, recipient=to_user, body=data['body'])
            Message.objects.create(user=to_user, sender=request.user, recipient=to_user, body=data['body'])
            return Response({'messages': 'message sent successfully'}, status=status.HTTP_201_CREATED)
        except:
            return Response({'messages': 'Form is not valid'}, status=status.HTTP_400_BAD_REQUEST)

class ConversationAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    # get user messages
    def get(self, request):
        print('--- get ---')
        messages_not_reading = Message.objects.filter(user=request.user, is_read=False)
        messages_reading = Message.objects.filter(user=request.user, is_read=True)

        serializer_messages_not_reading = ConversationSerializer(messages_not_reading, many=True)
        serializer_messages_reading = ConversationSerializer(messages_reading, many=True)
        return Response({
            'messages_not_reading': serializer_messages_not_reading.data,
            'messages_reading': serializer_messages_reading.data,
        }, status=status.HTTP_200_OK)