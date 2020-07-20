

from  rest_framework.permissions import IsAuthenticated
from knox.auth import TokenAuthentication
from posting.models import *
from rest_framework.renderers import JSONRenderer

from posting.serializers import *
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from posting.services import *
from recommendApp.detect import *
from .TextClassifier.Bi_LSTM.Classifier import text_detect
#from .darkflow import ImageDetection
import json

#UpLoadPosting

# class test(APIView):
#
#     permission_classes = [
#         permissions.IsAuthenticated,
#     ]
#
#     def post(self, request, format=None):
#
#         query = request.data['query']
#         result = text_detect(query)
#
#         print('result: ', result)
#         return Response(1)

class UpLoadPosting(APIView):
    renderer_classes = [JSONRenderer]

    authentication_classes = [TokenAuthentication, ]
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def get(self, request, format=None):
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        # upload_serializer = UploadSerializer(data=request.data)
        #
        # if upload_serializer.is_valid():
        #     upload_serializer.save()
        #     img_url = upload_serializer.data['image']
        #     results = ImageDetection.getItemName(img_url)
        #     print(results)
        #     return Response(results, status=status.HTTP_201_CREATED)

        # return Response("z", status=status.HTTP_201_CREATED)
        #Request값 받기
        user_id= request.user.idx
        #posting_cnt +1
        userPostCnt(user_id)

        #export to deepLearning Module
        post_id = currentPostId()+1
        print(post_id)#test
        #imageScore=AnalyzeImage(post_id)
        #textSocre=AnalyzeText(post_id)

        check = True

        # user_id 추가
        request.data.__setitem__("user_idx",
                                 request.user.idx)  # request.data에 key,value 추가하고 싶을 때 __setitem__(key,value)
        request.data.__setitem__("like_cnt", 0)  # request.data에 key,value 추가하고 싶을 때 __setitem__(key,value)
        serializer = UserPlaceHistorySerializer(data=request.data)

        imageResults = []
        imageScore = dict()





        if serializer.is_valid():
            serializer.save()
            #textResults=Grade(serializer.data['context'])
            #print(textResults)
            if serializer.data['img_1']:
                imageResults.append(image_detect(serializer.data['img_1']))
            if serializer.data['img_2']:
                imageResults.append(image_detect(serializer.data['img_2']))
            if serializer.data['img_3']:
                imageResults.append(image_detect(serializer.data['img_3']))
            if serializer.data['img_4']:
                imageResults.append(image_detect(serializer.data['img_4']))
            if serializer.data['img_5']:
                imageResults.append(image_detect(serializer.data['img_5']))
        print(imageResults)

        for result in imageResults:
            if len(result) !=0:
                for data in result:
                    imageScore[data.get('label')] = data.get('confidence')
                    insertImageScore(request,imageScore)
                    imageScore.clear()

        #텍스트 파싱
        textScore=dict()
        query = request.data['context']
        result = text_detect(query)
        print(result)
        for data in result:
            textScore[data.get('label')] =data.get('accuracy')
            insertTextScore(request, textScore)
            textScore.clear()

        #테스트
        # imageScore['칼국수']=1
        #textScore['매콤한']=1
        #Insert to UserPlaceHistory
        #check=insertUserPlaceHistory(request,post_id)

        #Insert to Score
        # if check==True:
        #     insertScore(request, imageScore, textScore)

        data=dict()
        data['check']=str(check)


        return Response(data, status=status.HTTP_201_CREATED)


