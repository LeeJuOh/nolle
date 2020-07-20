from  rest_framework.permissions import IsAuthenticated
from knox.auth import TokenAuthentication

from follow_map.models import *
from rest_framework.renderers import JSONRenderer

from follow_map.serializers import *
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from follow_map.services import *
import json

#CreateFollowMapActivity
class CreateFollowMapActivity(APIView):
    renderer_classes = [JSONRenderer]

    authentication_classes = [TokenAuthentication, ]
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def get(self, request, format=None):
        user = User.object.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        #Request값 받기
        user_id= request.data.get('user_idx')

        #user_follow에서 팔로잉유저들 찾기
        friends = []
        friends = search_following(user_id)

        #팔로잉 유저들의 카테고리 랭킹
        rank_category = []
        rank_category=rank_following(friends)

        #해당 카테고리 점수를 가진 팔로잉 유저들 반환
        followings = category_following(friends,rank_category)


        data = []
        data.append(rank_category)
        data.append(followings)

        print("data:",data)

        return Response(data, status=status.HTTP_201_CREATED)


