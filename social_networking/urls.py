from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static, serve
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),

    path('securelogin/', admin.site.urls),

    path('', views.home, name='home'),

    path('accounts/', include('accounts.urls')),
    path('', include('user_profile.urls')),
    path('', include('posting.urls')),
    path('', include('follow.urls')),
    path('', include('comment.urls')),
    path('', include('notifications.urls')),
    path('', include('conversations.urls')),

    # restapi
    path('api/', include('restapi.rest_urls.authentications_urls')),
    path('api/', include('restapi.rest_urls.follow_urls')),
    path('api/', include('restapi.rest_urls.posting_urls')),
    path('api/', include('restapi.rest_urls.notifications_urls')),
    path('api/', include('restapi.rest_urls.conversation_urls')),
    path('api/', include('restapi.rest_urls.user_profile_urls')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

