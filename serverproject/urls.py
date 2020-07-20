"""serverproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('voice_recognition/', include('voice_recognition.urls')),
    path('place_detail/', include('place_detail.urls')),
    path('follow_feed/',include('follow_feed.urls')),
    path('pick/',include('pick.urls')),
    path('posting/', include('posting.urls')),
    path('follow_map/', include('follow_map.urls')),
    path('follow_map_list/', include('follow_map_list.urls')),
    path('loginApp/', include('loginApp.urls')),
    path('commentApp/', include('commentApp.urls')),
    path('mypageApp/', include('mypageApp.urls')),
    path('recommendApp/', include('recommendApp.urls')),
    path('homeApp/', include('homeApp.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)