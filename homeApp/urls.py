from django.urls import path
from . import views

urlpatterns = [
    path('home2/', views.HomeListAPIView.as_view()), # 옛날꺼
    path('home/', views.HomeListAPIView2.as_view()), # 피어슨 완벽하게 구현
    path('search/', views.SearchListAPIView.as_view()),

]