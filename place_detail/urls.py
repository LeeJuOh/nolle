from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from place_detail import views

urlpatterns = [
    path('1/', views.CreatePlaceActivity.as_view()),
    path('2/', views.Pick_PlaceActivity.as_view()),

    #path('place_detail/1/', views.UserPlaceHistoryList.as_view()),
    path('place_detail/1/<int:pk>/', views.UserPlaceHistoryDetail.as_view()),
    path('place_detail/2/', views.UserPickList.as_view()),
    path('place_detail/2/<int:pk>/', views.UserPickDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)