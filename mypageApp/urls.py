from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('mypage/', views.MyPageDetail.as_view()),
    # path('userpage/', views.UserPageDetail.as_view()),
    path('userpage/<str:nickname>/', views.UserPageDetail.as_view()),
    path('myposting/', views.MyPostingList.as_view()),
    path('myfollow/', views.MyFollowList.as_view()),
    path('userfollow/<str:nickname>/', views.UserFollowList.as_view()),

    # path('managefollow/', views.ManageFollow.as_view()),
    path('managefollow/<str:nickname>/', views.ManageFollow.as_view())
]
