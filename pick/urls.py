from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from pick import views

urlpatterns = [
    path('1/', views.CreatePickActivity.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)