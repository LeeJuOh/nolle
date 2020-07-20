from django.shortcuts import render
from rest_framework import permissions, generics, status
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from knox.models import AuthToken
from .serializers import *
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.auth import TokenAuthentication
from django.contrib.auth import login


# Create your views here.
@api_view(["GET"])
def HelloAPI(request):

    print(request.user)
    return Response("hello world!")


class RegistrationAPI(generics.GenericAPIView):

    serializer_class = CreateUserSerializer

    def post(self, request, *args, **kwargs):
        if len(request.data["nickname"]) < 2 or len(request.data["password"]) < 4:
            body = {"message": "short field"}
            return Response(body, status=status.HTTP_400_BAD_REQUEST)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        return Response(
            {
                # "user": UserSerializer(
                #     user, context=self.get_serializer_context()
                # ).data,
                "user": UserSerializer(
                    user
                ).data,

                "token": AuthToken.objects.create(user)[1],
            }
        , status = status.HTTP_201_CREATED)


class LoginAPI(generics.GenericAPIView):
    # renderer_classes = [JSONRenderer]
    # 토큰인증은 username, password로 로그인 인증을 하는데
    # username : 가입 시 name 이므로 email 주소이다.. 씨발;
    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        login_user = User.object.get(idx = user.idx)
        return Response({
            # "user": UserSerializer(user,
            #                        context=self.get_serializer_context()).data['nickname'],
            "user": UserSerializer(login_user).data,
            "token": AuthToken.objects.create(user)[1]
        })


class UserAPI(generics.RetrieveAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    serializer_class = UserSerializer

    def get_object(self):


        return self.request.user
