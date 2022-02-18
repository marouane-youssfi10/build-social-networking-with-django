from django.urls import path, include
from rest_framework import routers

from restapi.rest_views.posting_views import (
    PostingProjectAPIView,
    PostingJobAPIView,
    PostingProjectViewsets,
    PostingJobViewsets,

    get_user_post_project,
    get_user_post_job,

    DeleteTagsProjectsViewsets,
    DeleteTagsJobsViewsets
)

router = routers.DefaultRouter()

# post project or job section
router.register('projects', PostingProjectViewsets, basename='projects')
router.register('jobs', PostingJobViewsets, basename='jobs')

# delete post section
router.register('delete-tags-project', DeleteTagsProjectsViewsets, basename='delete-tags-project')
router.register('delete-tags-job', DeleteTagsJobsViewsets, basename='delete-tags-jobs')

urlpatterns = [
    path('', include(router.urls)),

    path('posting-user-projects/', PostingProjectAPIView.as_view(), name='user-projects'),
    path('posting-user-jobs/', PostingJobAPIView.as_view(), name='user-jobs'),

    path('project/<int:pk>/', get_user_post_project, name='user-post-project'),
    path('job/<int:pk>/', get_user_post_job, name='user-post-job'),

]