from django.urls import path
from . import views

urlpatterns = [
    path('comment/', views.CommentListAPIView.as_view()),
    path('comment/<int:posting_idx>/', views.CommentListAPIView.as_view()),
    path('comment/detail/<int:idx>/', views.CommentDetailAPIView.as_view()),
    # path('userpage/', views.UserPageDetail.as_view()),
    # path('comment/', views.UserPageDetail.as_view()),
]