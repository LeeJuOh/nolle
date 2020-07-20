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


# def euclidean_distance(other_pt, user_pt):
#     distance = 0
#     for i in range(len(other_pt)):
#         distance += (other_pt[i] - user_pt[i]) ** 2
#     return distance ** 0.5

def get_home_recommend2(request_user):


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

    image_score_len =len(image_score)
    text_score_len = len(text_score)
    print('len image score: ', image_score_len)
    print('len text score: ', text_score_len)

    if image_score_len == 0 and text_score_len == 0:
        print("00 case >> user_pt: ")
        return None

    add_score = image_score + text_score
    add_score_len = len(add_score)
    print('add image and text score: ', add_score)
    print('len add score: ', add_score_len)


    user_pt = list()
    others_image = list()
    others_text= list()
    add_others = list()
    other_pt = list()
    other_user_idx = list()
    recommend_user = list()
    distance = list()
    user_idx = list()

    for idx,val in enumerate(add_score):
        user_pt.append(val['avg_score'])
        if idx < image_score_len:
            others_image.append(getOtherImageScoreList(val['level'], val['image_ctgr_idx'], request_user.idx))
        else:
            others_text.append(getOtherTextScoreList(val['level'], val['text_ctgr_idx'], request_user.idx))

    add_others = others_image + others_text
    add_others_len = len(add_others)
    print('add_others: ', add_others)
    print('add_others_len:  ', add_others_len)

    for vals in add_others:
        for val in vals:
            other_user_idx.append(val['user_idx'])

    other_user_idx = list(set(other_user_idx))
    other_user_idx_len = len(other_user_idx)
    print('other user idx: ', other_user_idx)
    print('other user idx len: ', other_user_idx_len)

    for val in other_user_idx:
        pt = list()
        for val_others in add_others:
            size =len(val_others)
            for idx, val_other in enumerate(val_others):
                if val == val_other['user_idx']:

                    pt.append(val_other['avg_score'])

                else :
                    print('none score')
                    if (idx+1) == size:
                        pt.append(0)

        other_pt.append(pt)

    user_pt_len = len(user_pt)
    other_pt_len = len(other_pt)

    print('user_pt: ', user_pt)
    print('user_pt_len: ', user_pt_len)

    print('other_pt: ', other_pt)
    print('len other_pt: ', other_pt_len)


    cal = list()
    print("pearson_similarity")
    cal = pearson_similarity(other_pt, user_pt, other_user_idx)
    distance = sorted(cal, key=operator.itemgetter(1), reverse=True)
    print("sorted : ", distance)


    for val in distance:
        recommend_user.append(User.object.get(idx=val[0]))
        if len(recommend_user) == 5:
            print('stop')
            break

    # recommend_user = list(set(recommend_user))
    print("user idx: ", recommend_user)
    return recommend_user
