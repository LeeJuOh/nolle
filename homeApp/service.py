from .models import *
from recommendApp.models import CategoryImageS, CategoryImageM, ImageSHistory, ImageMHistory, TextSHistory, TextMHistory
import random
from django.db.models import Avg, Max, Min, Sum
from django.db.models import Count
from operator import itemgetter
from django.db.models import Q
import numpy as np
import pandas as pd
import operator

def get_random_m():
    category_list = list()

    while True:

        if len(category_list) < 4:
            category_list.append(CategoryImageM.objects.order_by("?").first())
            category_list = list(set(category_list))
            if len(category_list) == 4:
                break;

    return category_list


def get_random_s():
    category_list = list()

    while True:

        if len(category_list) < 4:
            category_list.append(CategoryImageS.objects.order_by("?").first())
            category_list = list(set(category_list))
            if len(category_list) == 4:
                break;

    return category_list


def getUpdateHistory_image_s(request_user, weight):
    user = request_user
    image_s = ImageSScore.objects.values('image_ctgr_idx').annotate(avg_score=Avg('score')).filter(user_idx=user)
    image_s_history = ImageSHistory.objects.values('ctgr_idx').annotate(cnt=Count('ctgr_idx')).filter(user_idx=user)
    print(image_s)
    print(image_s_history)

    image_s = list(image_s)
    image_s_history = list(image_s_history)
    for image in image_s:
        image['level'] = 'S'

        for idx,history in enumerate(image_s_history):
            if image['image_ctgr_idx'] == history['ctgr_idx']:
                print("update socre")
                image['avg_score'] = image['avg_score'] + history['cnt'] * weight
                image_s_history.pop(idx)


    for history in image_s_history:
        image_s.append({'image_ctgr_idx': history['ctgr_idx'], 'avg_score': history['cnt'] * weight, 'level': 'S'})

    print("updated image_s" , image_s)
    # print(image_s_history)
    print('--------------------------------------------------------')

    return image_s


def getUpdateHistory_image_m(request_user,weight):
    user = request_user
    image_m = ImageMScore.objects.values('image_ctgr_idx').annotate(avg_score=Avg('score')).filter(user_idx=user)
    image_m_history = ImageMHistory.objects.values('ctgr_idx').annotate(cnt=Count('ctgr_idx')).filter(user_idx=user)
    print(image_m)
    print(image_m_history)

    image_m = list(image_m)
    image_m_history = list(image_m_history)
    for image in image_m:
        image['level'] = 'M'

        for idx,history in enumerate(image_m_history):
            if image['image_ctgr_idx'] == history['ctgr_idx']:
                print("update socre")
                image['avg_score'] = image['avg_score'] + history['cnt'] * weight
                image_m_history.pop(idx)

    for history in image_m_history:
        image_m.append({'image_ctgr_idx': history['ctgr_idx'], 'avg_score': history['cnt'] * weight, 'level': 'M'})

    print("updated image_m" ,image_m)
    # print(image_m_history)
    print('--------------------------------------------------------')
    return image_m


def getUpdateHistory_text_s(request_user, weight):
    user = request_user
    text_s = TextSScore.objects.values('text_ctgr_idx').annotate(avg_score=Avg('score')).filter(user_idx=user)
    text_s_history = TextSHistory.objects.values('ctgr_idx').annotate(cnt=Count('ctgr_idx')).filter(user_idx=user)
    print(text_s)
    print(text_s_history)

    text_s = list(text_s)
    text_s_history = list(text_s_history)
    for text in text_s:
        text['level'] = 'S'
        for idx,history in enumerate(text_s_history):
            if text['text_ctgr_idx'] == history['ctgr_idx']:
                print("update socre")
                text['avg_score'] = text['avg_score'] + history['cnt'] * weight
                text_s_history.pop(idx)

    for history in text_s_history:
        text_s.append({'text_ctgr_idx': history['ctgr_idx'], 'avg_score': history['cnt'] * weight, 'level': 'S'})

    print("updated text_s" ,text_s)
    # print(text_s_history)
    print('--------------------------------------------------------')
    return text_s


def getUpdateHistory_text_m(request_user, weight):
    user = request_user
    text_m = TextMScore.objects.values('text_ctgr_idx').annotate(avg_score=Avg('score')).filter(user_idx=user)
    text_m_history = TextMHistory.objects.values('ctgr_idx').annotate(cnt=Count('ctgr_idx')).filter(user_idx=user)
    print(text_m)
    print(text_m_history)

    text_m = list(text_m)
    text_m_history = list(text_m_history)
    for text in text_m:
        text['level'] = 'M'
        for idx,history in enumerate(text_m_history):
            if text['text_ctgr_idx'] == history['ctgr_idx']:
                print("update socre")
                text['avg_score'] = text['avg_score'] + history['cnt'] * weight
                text_m_history.pop(idx)

    for history in text_m_history:
        text_m.append({'text_ctgr_idx': history['ctgr_idx'], 'avg_score': history['cnt'] * weight, 'level': 'S'})

    print("updated text_m" ,text_m)
    # print(text_m_history)
    print('--------------------------------------------------------')
    return text_m


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


def pearson_similarity(other_pt , user_pt, user_idx):

    lst = other_pt
    lst.insert(0, user_pt)
    print(lst)
    df =pd.DataFrame(lst).T

    corr =df.corr(method = 'pearson')
    corr.fillna(0)

    index_list = corr[0].index.tolist()

    value_list = corr[0].fillna(0).values.tolist()

    return_list = list()
    length = len(value_list)
    for i in range(1, length) :
        return_list.append([user_idx[i-1], value_list[i]])
    print('return pearson: ', return_list)
    return return_list


def euclidean_distance(other_pt, user_pt):
    distance = 0
    for i in range(len(other_pt)):
        distance += (other_pt[i] - user_pt[i]) ** 2
    return distance ** 0.5

def get_home_recommend(request_user):


    weight = 0.5
    image_s_history = getUpdateHistory_image_s(request_user, weight)
    image_m_history = getUpdateHistory_image_m(request_user, weight)
    text_s_history = getUpdateHistory_text_s(request_user, weight)
    text_m_history = getUpdateHistory_text_m(request_user, weight)

    image_score = image_s_history + image_m_history
    image_score = sorted(image_score, key=itemgetter('avg_score'), reverse=True)
    print("sorted image score : ", image_score)
    text_score = text_s_history + text_m_history
    text_score = sorted(text_score, key=itemgetter('avg_score'), reverse=True)
    print("sorted text score : ", text_score)

    print('len image score: ', len(image_score))
    print('len text score: ', len(text_score))

    loop = 0
    if len(image_score) == 0 and len(text_score) == 0:
        user_pt = [0,0]
        print("00 case >> user_pt: ", user_pt)
        return None

    elif len(image_score) == 0 :
        loop = len(text_score)
    elif len(text_score) == 0:
        loop = len(image_score)

    elif len(image_score) >= len(text_score) :
        loop = len(text_score)
    elif len(image_score) <= len(text_score) :
        loop = len(image_score)


    print("loop: ", loop)
    other_pt = list()
    recommend_user = list()
    distance = list()
    user_idx = list()
    for idx in range(loop):

        if len(image_score) == 0 and len(text_score) >= 1:
            t_score = text_score[idx]
            print('t_score: ', t_score)

            user_pt = [0, t_score['avg_score']]
            print("01 case >> user_pt: ", user_pt)
            others_text = getOtherTextScoreList(t_score['level'], t_score['text_ctgr_idx'], request_user.idx)
            print('others_text', others_text)
            for text in others_text:

                other_pt.append([0, text.get('avg_score')])
                print("other pt: ", [0, text.get('avg_score')])
                user_idx.append(text.get('user_idx'))

        elif len(image_score) >= 1 and len(text_score) == 0:
            i_score = image_score[idx]
            print('i_score: ', i_score)

            user_pt = [i_score['avg_score'], 0]
            print("10 case >> user_pt: ", user_pt)
            others_image = getOtherImageScoreList(i_score['level'], i_score['image_ctgr_idx'],
                                                  request_user.idx)
            print('others_image', others_image)
            for image in others_image:

                other_pt.append([image.get('avg_score'), 0])
                print("other pt: ", [image.get('avg_score'), 0])
                user_idx.append(image.get('user_idx'))
        else:
            t_score = text_score[idx]
            i_score = image_score[idx]
            print('i_score: ', i_score)
            print('t_score: ', t_score)


            user_pt = [i_score['avg_score'], t_score['avg_score']]
            print("11 case >> user_pt: ", user_pt)

            others_image = getOtherImageScoreList(i_score['level'], i_score['image_ctgr_idx'], request_user.idx)
            others_text = getOtherTextScoreList(t_score['level'], t_score['text_ctgr_idx'], request_user.idx)

            print('others_text', others_text)
            print('others_image', others_image)
            for image in others_image:
                for text in others_text:
                    if image.get('user_idx') == text.get('user_idx'):
                        print("find : ", image.get('user_idx'), ", ", text.get('user_idx'))
                        other_pt.append([image.get('avg_score'), text.get('avg_score')])
                        print("other pt: ", [image.get('avg_score'), text.get('avg_score')])
                        user_idx.append(image.get('user_idx'))


    print('user_pt', user_pt)

    print('other idx: ', user_idx)
    print('other idx len: ', len(user_idx))
    print("other: ", other_pt)
    print('other pt len: ', len(other_pt))
    cal = list()
    if user_pt == [0,0]:
        print("euclidean_distance")
        for idx, val in enumerate(other_pt):
            cal.append((others_image[idx].get('user_idx'), euclidean_distance(val, user_pt)))
        # distance += sorted(cal, key=operator.itemgetter(1))
        distance += cal

        # distance = list(set(distance))
        print("distance : ", distance)

    else :
        print("pearson_similarity")
        cal = pearson_similarity(other_pt, user_pt, user_idx)
        # distance += sorted(cal, key=operator.itemgetter(1), reverse = True)
        # print("sorted : ", distance)
        distance += cal

        # distance = list(set(distance))
        print("distance : ", distance)

    distance = list(set(map(tuple, distance)))
    print('dp: ', distance)

    distance = sorted(distance, key=operator.itemgetter(1), reverse=True)
    print("sorted : ", distance)


    for val in distance:
        recommend_user.append(User.object.get(idx=val[0]))
        if len(recommend_user) == 5:
            print('stop')
            break

    # recommend_user = list(set(recommend_user))
    print("user idx: ", recommend_user)
    return recommend_user
