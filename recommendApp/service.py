from konlpy.tag import Kkma
from .models import *
import re
from django.db.models import Avg, Max, Min, Sum
import operator
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
from itertools import chain
import numpy as np
import pandas as pd
from operator import itemgetter
def test():

    sentence = "놀거리 추천해줘"
    kkma = Kkma()

    print(kkma.pos(sentence))
    munjang=kkma.morphs(sentence)

    text = CategoryTextS.objects.all()
    image = CategoryImageS.objects.all()

    for ts in image:
        if ts.ctgr_name in sentence:

            print("예",ts.ctgr_name)

    for ts in text:
        if ts.ctgr_name in munjang:
        # if re.search('^' + ts.ctgr_name, munjang):

            print("예",ts.ctgr_name)
    for val in text:
        print(val.ctgr_name, ": ", kkma.pos(val.ctgr_name), "/ ",kkma.nouns(val.ctgr_name))
        print()



def getKeyword_list(request_sentence):

    # sentence = request_sentence
    kkma = Kkma()
    print(kkma.pos(request_sentence))
    print(kkma.nouns(request_sentence))

    keyword_list = kkma.morphs(request_sentence)
    print(keyword_list)

    return keyword_list


def getImageKeyword(request_sentence, user):
    matching_image = list()

    for category in CategoryImageS.objects.all():
        if category.ctgr_name in request_sentence:
            print("image_S: " + category.ctgr_name)
            matching_image.append(('S', 'image', category.ctgr_sid, category.ctgr_name))
            ImageSHistory.objects.create(user_idx=user, ctgr_idx=category)
            break;

    if len(matching_image) == 0:
        for category in CategoryImageM.objects.all():
            if category.ctgr_name in request_sentence:
                print("image_M: " + category.ctgr_name)
                matching_image.append(('M', 'image', category.ctgr_mid, category.ctgr_name))
                ImageSHistory.objects.create(user_idx=user, ctgr_idx=category)
                break;

    return matching_image


def getTextKeyword(keyword_list,user):
    matching_text = list()

    for category in CategoryTextS.objects.all():
        if category.ctgr_name in keyword_list:
            print("TEXT_S: " + category.ctgr_name)
            matching_text.append(('S', 'text', category.ctgr_id, category.ctgr_name))
            TextSHistory.objects.create(user_idx=user, ctgr_idx=category)
            break;

    if len(matching_text) == 0:
        for category in CategoryTextM.objects.all():
            if category.ctgr_name in keyword_list:
                print("TEXT_M: " + category.ctgr_name)
                matching_text.append(('M', 'text', category.ctgr_id, category.ctgr_name))
                TextMHistory.objects.create(user_idx=user, ctgr_idx=category)
                break;

    return matching_text


def getLargeKeyword(request_sentence, user):
    matching = list()
    for category in CategoryL.objects.all():
        if category.ctgr_name in request_sentence:
            print("L: " + category.ctgr_name)
            matching.append(('L', category.ctgr_lid, category.ctgr_name))
            UserLHistory.objects.create(user_idx=user, ctgr_idx=category)
            break;

    return matching



def getOtherImageScoreList(image_level, image_cg_idx, user_idx):
    if image_level == 'S':

        others_image = ImageSScore.objects.values('user_idx').annotate(avg_score=Avg('score')).filter(
            image_ctgr_idx=image_cg_idx).exclude(user_idx=user_idx)

    else:
        others_image = ImageMScore.objects.values('user_idx').annotate(avg_score=Avg('score')).filter(
            image_ctgr_idx=image_cg_idx).exclude(user_idx=user_idx)

    try:
        return others_image
    except others_image.DoesNotExist:
        print("doesnotexist")




def getOtherTextScoreList(text_level, text_cg_idx, user_idx):
    if text_level == 'S':

        others_text = TextSScore.objects.values('user_idx').annotate(avg_score=Avg('score')).filter(
            text_ctgr_idx=text_cg_idx).exclude(user_idx=user_idx)

    else:

        others_text = TextMScore.objects.values('user_idx').annotate(avg_score=Avg('score')).filter(
            text_ctgr_idx=text_cg_idx).exclude(user_idx=user_idx)

    try:
        return others_text
    except others_text.DoesNotExist:
        print("doesnotexist")


def getRecommend(request_sentence, request_user):
    user = request_user
    sentence = request_sentence
    user_idx = user.idx

    keyword_list = getKeyword_list(sentence)
    matching_image = getImageKeyword(sentence, user)
    matching_text = getTextKeyword(keyword_list, user)

    matching_image_len = len(matching_image)
    matching_text_len = len(matching_text)

    print(matching_image)
    print(matching_text)
    others_text =list()
    others_image = list()
    other_pt = list()
    user_idx_list= list()
    # user_pt  = [0,0]
    if matching_image_len == 0 and matching_text_len == 0:

        matching = getLargeKeyword(keyword_list, user)
        print(matching)
        if len(matching) == 0:
            print("nothing matching")
            return None

    elif matching_image_len == 0 and matching_text_len >= 1:

        text_level = matching_text[0][0]
        text_cg_idx = matching_text[0][2]

        others_text = getOtherTextScoreList(text_level, text_cg_idx, user_idx)

        print('other text', others_text)
        for text in others_text:
            print("other pt: ", [0, text.get('avg_score')])
            other_pt.append([0, text.get('avg_score')])

    elif matching_image_len >= 1 and matching_text_len == 0:

        image_level = matching_image[0][0]
        image_cg_idx = matching_image[0][2]

        others_image = getOtherImageScoreList(image_level, image_cg_idx, user_idx)
        print('other image', others_image)

        for image in others_image:
            print("other pt: ", [image.get('avg_score'), 0])
            other_pt.append([image.get('avg_score'), 0])

    else:
        print("else")
        image_level = matching_image[0][0]
        image_cg_idx = matching_image[0][2]

        text_level = matching_text[0][0]
        text_cg_idx = matching_text[0][2]

        others_image = getOtherImageScoreList(image_level, image_cg_idx, user_idx)
        others_text = getOtherTextScoreList(text_level, text_cg_idx, user_idx)
        print('other image', others_image)
        print('other text', others_text)

        for image in others_image:
            for text in others_text:
                if image.get('user_idx') == text.get('user_idx'):
                    print("find : ", image.get('user_idx'), ", ", text.get('user_idx'))
                    other_pt.append([image.get('avg_score'), text.get('avg_score')])
                    print("other pt: ", [image.get('avg_score'), text.get('avg_score')])
                    user_idx_list.append(image.get('user_idx'))

    others_image_len = len(others_image)
    others_text_len = len(others_text)

    cal = list()
    if others_image_len == 0 and others_text_len == 0 :
        return None
    elif others_image_len >= 1 and others_text_len == 0 :
        for idx, val in enumerate(other_pt):
            cal.append((others_image[idx].get('user_idx'), euclidean_distance(val)))
    elif others_image_len == 0 and others_text_len <= 1:
        for idx, val in enumerate(other_pt):
            cal.append((others_text[idx].get('user_idx'), euclidean_distance(val)))

    else :
        for idx, val in enumerate(other_pt):
            cal.append((user_idx_list[idx], euclidean_distance(val)))

    distance = cal
    distance = list(set(distance))
    distance = sorted(distance, key=itemgetter(1), reverse = True)

    print('distance', distance)
    print("user idx: ", distance)

    user_list = list()
    for val in distance:
        user_list.append(User.object.get(idx = val[0]))
        if len(user_list) == 5:
            break;

    print(user_list)
    return user_list


def imgae_search(results, user):
    #
    # label = results[0]['label']
    # accuracy = results[0]['confidence']
    other_image_socre_list = list()
    try:
        for result in results :
            image_s = CategoryImageS.objects.filter(ctgr_name_en = result['label'])
            print(image_s)
            for s in image_s:
                other_image_score = getOtherImageScoreList('S', s, user)
                other_image_socre_list.append(other_image_score)
                ImageSHistory.objects.create(user_idx=user, ctgr_idx=s)

    except CategoryImageS.DoesNotExist:
        print("제공하지 않는 품목")
        return None
    print('matching_image_list : ', other_image_socre_list)

    # user_pt = [0,0]
    other_pt = list()
    user_idx = list()
    cal = list()
    for other_image_score in other_image_socre_list:
        for image in other_image_score:
            print("matching pt: ", [image.get('avg_score'), 0])
            other_pt.append([image.get('avg_score'), 0])
            user_idx.append(image.get('user_idx'))

    print('other pt: ',other_pt)
    print('user_idx: ',user_idx)
    for idx, val in enumerate(other_pt):
        cal.append((user_idx[idx], euclidean_distance(val)))

    distance = cal
    distance = list(set(distance))
    distance = sorted(distance, key=itemgetter(1), reverse=True)
    print("distance: ", distance)

    user_list = list()
    for val in distance:
        user_list.append(User.object.get(idx = val[0]))
        if len(user_list) == 5:
            break;
    print(user_list)
    return user_list

def euclidean_distance(other_pt):
    distance = 0
    user_pt = [0,0]
    for i in range(len(other_pt)):
        distance += (other_pt[i] - user_pt[i]) ** 2
    return distance ** 0.5

# def getUserName(user_idx):
#
#     return User.object.get(idx = user_idx).user_nm
