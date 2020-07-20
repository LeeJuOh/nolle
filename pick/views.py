from  rest_framework.permissions import IsAuthenticated
from knox.auth import TokenAuthentication
from pick.models import User
from pick.models import UserPick
from rest_framework.renderers import JSONRenderer

from pick.serializers import *
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
import json

#CreatePickActivity
class CreatePickActivity(APIView):
    renderer_classes = [JSONRenderer]

    authentication_classes = [TokenAuthentication, ]
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def get(self, request, format=None):
        userpick = UserPick.objects.all()
        serializer = UserPickSerializer(userpick, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        user_id= request.user.idx
        rating=0.0
        userpick = UserPick.objects.all()
        data= []
        #UserPick Tb에서 해당 User의 pick한 장소 찾기
        for pick in userpick:
            if pick.user_idx.idx == int(user_id):
                print(pick)
                temp = dict()
                temp["place_id"] = pick.place_id
                data.append(temp)
                print(data)

        return Response({


            "pick": data

        })


