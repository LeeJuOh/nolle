from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from rest_framework import permissions
from knox.auth import TokenAuthentication
from .models import *

# Create your views here.
class MyPageDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """

    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def get(self, request, format=None):

        print(request.data)
        serializer = MyPageSerializer(request.user)
        return Response({
            "mypage": serializer.data
        })

    def put(self, request, format=None):
        serializer = UserSerializer(request.user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"mypage":serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):

        request.user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserPageDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """

    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def get_object(self, nickname):
        try:
            return User.object.get(nickname=nickname)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, nickname, format=None):
        user_page = self.get_object(nickname)
        serializer = UserPageSerializer(user_page)

        # 포스팅 썸네일 = place_id 일단,, 이거 바꿔야함 image필드로
        return Response({

            "userpage" : serializer.data
        })

class MyPostingList(APIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def get(self, request, format=None):
        posting = UserPlaceHistory.objects.filter(user_idx = request.user)
        serializer = UserPlaceHistorySerializer(posting, many=True)

        return Response({

            "my_posting" : serializer.data
        })


class MyFollowList(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """

    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def get(self, request, format=None):

        user = request.user
        serializer = UserFollowSerializer(user)

        return Response({

            "follow" : serializer.data
        })




class UserFollowList(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """

    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def get(self, request, nickname, format=None):

        user = User.object.get(nickname = nickname)
        serializer = UserFollowSerializer(user)

        # 포스팅 썸네일 = place_id 일단,, 이거 바꿔야함 image필드로
        return Response({

            "follow" : serializer.data
        })




class ManageFollow(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """

    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def get(self, request,nickname):
        user = request.user
        other_user = User.object.get(nickname=nickname)

        try:
            follow = UserFollow.objects.get(user_idx=user, following_idx=other_user)
            follow = UserFollow.objects.get(user_idx = user, following_idx = other_user)
            follow.delete()
            user.following_cnt = user.following_cnt - 1
            other_user.follower_cnt = other_user.follower_cnt - 1
            user.save()
            other_user.save()
            return Response({
                "code" : 101,
                "msg" : "팔로우 삭제"
            })
        except UserFollow.DoesNotExist:
            follow = UserFollow.objects.create(user_idx = user, following_idx = other_user)
            follow.save()

            user.following_cnt = user.following_cnt + 1
            other_user.follower_cnt = other_user.follower_cnt + 1
            user.save()
            other_user.save()

            return Response({
                "code" : 100,
                "msg" : "팔로우 성공"
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    # def delete(self, request, nickname):
    #     user = request.user
    #     other_user = User.object.get(nickname=nickname)
    #     try:
    #         follow = UserFollow.objects.get(user_idx = user, following_idx = other_user)
    #         follow.delete()
    #         user.following_cnt = user.following_cnt - 1
    #         other_user.follower_cnt = other_user.follower_cnt - 1
    #         user.save()
    #         other_user.save()
    #
    #     except UserFollow.DoesNotExist:
    #         return Response({
    #             "code" : 101,
    #             "msg" : "팔로우 상태가 아닙니다."
    #         })
    #
    #     return Response(status=status.HTTP_204_NO_CONTENT)