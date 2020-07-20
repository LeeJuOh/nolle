from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from follow_map import views
from knox import views as knox_views

urlpatterns = [
    path('1/', views.CreateFollowMapActivity.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)