from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from posting import views

urlpatterns = [
    path('1/', views.UpLoadPosting.as_view()),
    # path('2/', views.test.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)