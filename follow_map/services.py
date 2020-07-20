from follow_map.models import *
from follow_map.serializers import *
def search_following(user_id):
    user_follow = UserFollow.objects.all()

    following = []
    for users in user_follow:
        if users.user_idx.idx == int(user_id):
            following.append(users.following_idx.idx)

    print(following)
    return following

def rank_following(following):
    text_m_score=TextMScore.objects.all()
    image_m_score=ImageMScore.objects.all()
    text = dict()
    image = dict()
    #해당 유저의
    for user in following:
        #갖고 있는 카테고리의 score값 저장
        for score in text_m_score:
            if user == score.user_idx.idx:
                if text.get(score.text_ctgr_idx.ctgr_id) == None:
                    text[score.text_ctgr_idx.ctgr_id]=score.score
                else:
                    text[score.text_ctgr_idx.ctgr_id]+=score.score
        for score in image_m_score:
            if user == score.user_idx.idx:
                if image.get(score.image_ctgr_idx.ctgr_mid) == None:
                    image[score.image_ctgr_idx.ctgr_mid]=score.score
                else:
                    image[score.image_ctgr_idx.ctgr_mid]+=score.score

    #image와 text 내림차순 분류
    image_sort = sorted(image.items(),key=(lambda x:x[1]),reverse = True)
    text_sort = sorted(text.items(), key=(lambda x: x[1]), reverse=True)


    texts=[]
    images=[]

    cnt = 0
    image_idx = 0
    text_idx = 0
    print("len:",len(image_sort))
    print("len:",len(text_sort))


    while (cnt <=5) and (image_idx < len(image_sort) or text_idx < len(text_sort)):
        if len(image_sort)==0:
            texts.append(text_sort.pop(image_idx)[0])
        elif len(text_sort)==0:
            images.append(image_sort.pop(image_idx)[0])
        else:
            if image_sort[image_idx][1] < text_sort[text_idx][1]:
                texts.append(text_sort.pop(image_idx)[0])
            else :
                images.append(image_sort.pop(image_idx)[0])
        cnt+=1

    category = dict()
    category['text'] = texts
    category['image'] = images

    print(category)

    return category

def category_following(friends,ranks):
    follow_user= []
    textMScore = TextMScore.objects.all()
    imageMScore = ImageMScore.objects.all()
    categoryImageM = CategoryImageM.objects
    categoryTextM = CategoryTextS.objects

    image_rank=ranks.get('image')
    text_rank=ranks.get('text')

    #{카테고리 번호 : 해당 유저 리스트}
    images=dict()
    texts=dict()

    # 이미지 카테고리 하나
    for image in image_rank:
        temp = []
        # 스코어 행 하나
        for score in imageMScore:
            if score.user_idx.idx in friends and score.image_ctgr_idx.ctgr_mid == image:
                if not(score.user_idx.idx in temp):
                    serializer = UserSerializer(score.user_idx)
                    temp.append(serializer.data)


        images[categoryImageM.get(ctgr_mid=image).ctgr_name] = temp

    # 텍스트 카테고리 하나
    for text in text_rank:
        temp = []
        # 텍스트 행 하나
        for score in textMScore:
            if score.user_idx.idx in friends and score.text_ctgr_idx.ctgr_id == text:
                if not(score.user_idx.idx in temp):
                    serializer = UserSerializer(score.user_idx)
                    temp.append(serializer.data)

        texts[categoryTextM.get(ctgr_id=text).ctgr_name] = temp


    category=dict()
    category['image']=images
    category['text']=texts

    return category