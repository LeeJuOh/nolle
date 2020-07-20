from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from rest_framework import viewsets, permissions
from knox.auth import TokenAuthentication
from .service import get_random_m, get_random_s, get_home_recommend
from .service2 import *
from .models import *


# Create your views here.

class HomeListAPIView(APIView):

    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def get(self, request):

        user = request.user
        query_set = get_home_recommend(user)

        if query_set is None or len(query_set) == 0:
            print('none')
            filter = UserPlaceHistory.objects.filter().order_by('-like_cnt').exclude(user_idx=request.user)
            rows = filter.values('user_idx').distinct()[:5]
            rows_removed_deduplication = list(
                {rows['user_idx']: rows for rows in rows}.values())
            print(rows_removed_deduplication)
            query = list()
            for row in rows_removed_deduplication:
                user = User.object.get(idx=row['user_idx'])
                query.append(user)

            home_serializer = HomeSerializer(query, many=True)
        else:
            home_serializer = HomeSerializer(query_set, many=True)

        # user_pick = user.home_userpick_set.all()
        # pick_serializer = PickPlaceSerializer(user_pick, many=True)


        realtime_reviews = UserPlaceHistory.objects.all().order_by('-date')[:8]
        real_serializer = UserPlaceHistorySerializer(realtime_reviews, many=True)

        hot_reviews = UserPlaceHistory.objects.all().order_by('-like_cnt')[:8]
        hot_serializer = UserPlaceHistorySerializer(hot_reviews, many=True)

        category_m = get_random_m()
        category_m_serializer = CategoryImageMSerializer(category_m, many=True)

        category_s = get_random_s()
        category_s_serializer = CategoryImageSSerializer(category_s, many= True)


        return Response({
            "home_recommendation":home_serializer.data,
            # "user_pick" : pick_serializer.data,
            "real_time": real_serializer.data,
            "hot": hot_serializer.data,
            "category_m": category_m_serializer.data,
            "category_s": category_s_serializer.data

        })
class HomeListAPIView2(APIView):

    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def get(self, request):

        user = request.user
        query_set = get_home_recommend2(user)

        if query_set is None or len(query_set) == 0:
            print('none')
            filter = UserPlaceHistory.objects.filter().order_by('-like_cnt').exclude(user_idx=request.user)
            rows = filter.values('user_idx').distinct()[:5]
            rows_removed_deduplication = list(
                {rows['user_idx']: rows for rows in rows}.values())
            print(rows_removed_deduplication)
            query = list()
            for row in rows_removed_deduplication:
                user = User.object.get(idx=row['user_idx'])
                query.append(user)

            home_serializer = HomeSerializer(query, many=True)
        else:
            home_serializer = HomeSerializer(query_set, many=True)

        # user_pick = user.home_userpick_set.all()
        # pick_serializer = PickPlaceSerializer(user_pick, many=True)


        realtime_reviews = UserPlaceHistory.objects.all().order_by('-date')[:8]
        real_serializer = UserPlaceHistorySerializer(realtime_reviews, many=True)

        hot_reviews = UserPlaceHistory.objects.all().order_by('-like_cnt')[:8]
        hot_serializer = UserPlaceHistorySerializer(hot_reviews, many=True)

        category_m = get_random_m()
        category_m_serializer = CategoryImageMSerializer(category_m, many=True)

        category_s = get_random_s()
        category_s_serializer = CategoryImageSSerializer(category_s, many= True)


        return Response({
            "home_recommendation":home_serializer.data,
            # "user_pick" : pick_serializer.data,
            "real_time": real_serializer.data,
            "hot": hot_serializer.data,
            "category_m": category_m_serializer.data,
            "category_s": category_s_serializer.data

        })

class SearchListAPIView(APIView):

    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def get(self, request):

        user = request.user
        query_set = get_home_recommend2(user)

        if query_set is None or len(query_set) == 0:
            print('none')
            filter = UserPlaceHistory.objects.filter().order_by('-like_cnt').exclude(user_idx=request.user)
            rows = filter.values('user_idx').distinct()[:5]
            rows_removed_deduplication = list(
                {rows['user_idx']: rows for rows in rows}.values())
            print(rows_removed_deduplication)
            query = list()
            for row in rows_removed_deduplication:
                user = User.object.get(idx=row['user_idx'])
                query.append(user)

            home_serializer = HomeSerializer(query, many=True)
        else:
            home_serializer = HomeSerializer(query_set, many=True)

        # user_pick = user.userpick_set.all()
        # pick_serializer = PickPlaceSerializer(user_pick, many=True)

        realtime_reviews = UserPlaceHistory.objects.all().order_by('-date')[:8]
        real_serializer = UserPlaceHistorySerializer(realtime_reviews, many=True)

        hot_reviews = UserPlaceHistory.objects.all().order_by('-like_cnt')[:8]
        hot_serializer = UserPlaceHistorySerializer(hot_reviews, many=True)

        category_m = get_random_m()
        category_m_serializer = CategoryImageMSerializer(category_m, many=True)

        category_s = get_random_s()
        category_s_serializer = CategoryImageSSerializer(category_s, many= True)

        search_history = UserSearchHistory.objects
        filter = search_history.filter()
        rows = filter.values('text').distinct()
        print(rows)

        return Response({

            "home_recommendation":home_serializer.data,
            # "user_pick" : pick_serializer.data,
            "realtime_posting": real_serializer.data,
            "hot_posting": hot_serializer.data,
            "category_m": category_m_serializer.data,
            "category_s": category_s_serializer.data,
            "category_s": category_s_serializer.data,
            "search_history": rows,

        })