"""social_networking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
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

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

