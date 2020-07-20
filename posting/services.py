from posting.models import *
from posting.serializers import *
def userPostCnt(user_id):
    users = User.object.all()

    for user in users:
        print("user",user)
        print(user.posting_cnt)
        if user.idx == int(user_id):
            print("발견0")
            user.posting_cnt+=1
            user.save()
            break

def currentPostId():
    post = UserPlaceHistory.objects.last()
    return post.idx

def insertUserPlaceHistory(request,post_id):
    print("request:  ",request.data)
    #user_id 추가
    request.data.__setitem__("user_idx",request.user.idx) #request.data에 key,value 추가하고 싶을 때 __setitem__(key,value)
    request.data.__setitem__("like_cnt",0) #request.data에 key,value 추가하고 싶을 때 __setitem__(key,value)
    serializer = UserPlaceHistorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return True
    print("adfaf",serializer.errors)
    return False

def insertTextScore(request,textScore):
    user_id = request.user.idx

    # TextScoreUpdate
    for textKey in textScore.keys():
        categoryM = CategoryTextM.objects.all()
        for category in categoryM:
            if category.ctgr_name == textKey:
                print("발견2")
                middle_id = category.ctgr_id

                # largeScore Update
                data = dict()

                # MiddleScore Update
                data.clear()
                data['user_idx'] = user_id
                data['text_ctgr_idx'] = middle_id
                data['score'] = textScore.get(textKey)
                data['posting_idx'] = currentPostId()
                print("middle text:", data)
                serializer = TextMScoreSerializer(data=data)
                if serializer.is_valid():
                    serializer.save()
                # SmallScore Update
                categoryS = CategoryTextS.objects.all()
                for category in categoryS:
                    if category.middle_id.ctgr_id == middle_id:
                        data.clear()
                        data['user_idx'] = user_id
                        data['text_ctgr_idx'] = category.ctgr_id
                        data['score'] = textScore.get(textKey)
                        data['posting_idx'] = currentPostId()
                        print("small_text:", data)
                        serializer = TextSScoreSerializer(data=data)
                        if serializer.is_valid():
                            serializer.save()

def insertImageScore(request,imageScore):
    user_id = request.user.idx

    #imageScoreUpdate
    for imageKey in imageScore.keys():
        categoryS = CategoryImageS.objects.all()
        valid = []
        for category in categoryS:
            if category.ctgr_name_en == imageKey:
                print("발견")
                small_id = category.ctgr_sid
                large_id = category.large_id.large_id.ctgr_lid
                middle_id = category.middle_id.ctgr_mid
                print(large_id,middle_id)
                #largeScore Update
                data=dict()

                #MiddleScore Update
                data.clear()
                data['user_idx']=user_id
                data['image_ctgr_idx']=middle_id
                data['score']=imageScore.get(imageKey)
                data['posting_idx']=currentPostId()
                print("middle_image:", data)
                serializer = ImageMScoreSerializer(data=data)
                if serializer.is_valid():
                    serializer.save()
                #SmallScore Update
                data.clear()
                if imageKey not in valid:
                    data['user_idx']=user_id
                    data['image_ctgr_idx']=small_id
                    data['score']=imageScore.get(imageKey)
                    data['posting_idx']=currentPostId()
                    print("small_image:", data)
                    serializer = ImageSScoreSerializer(data=data)
                    if serializer.is_valid():
                        print("valid")
                        serializer.save()
                        valid.append(imageKey)










