from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from follow_feed import views

urlpatterns = [
    path('1/', views.CreateFeedActivity.as_view()),
    path('2/', views.LikeViews.as_view()),
    path('3/', views.ReviewViews.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)