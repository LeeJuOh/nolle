# -*- coding: utf-8 -*-
"""
Created on Thu May 24 11:15:44 2018
@author: jbk48
@editor: lumyjuwon
"""
from django.apps import AppConfig
import os
import tensorflow as tf
from posting.TextClassifier.Bi_LSTM import Bi_LSTM as Bi_LSTM
from posting.TextClassifier.Bi_LSTM import Word2Vec as Word2Vec
import gensim
import numpy as np
import csv


def Convert2Vec(model_name, sentence):
    word_vec = []
    sub = []
    model = gensim.models.word2vec.Word2Vec.load(model_name)
    for word in sentence:
        if (word in model.wv.vocab):
            sub.append(model.wv[word])
        else:
            sub.append(np.random.uniform(-0.25, 0.25, 300))  # used for OOV words
    word_vec.append(sub)
    return word_vec


def Grade(sentence, W2V, Batch_size, Maxseq_length, Vector_size,prediction, X, seq_len, sess ):

    tokens = W2V.tokenize(sentence)

    embedding = Convert2Vec('./posting/TextClassifier/Bi_LSTM/Data/post.embedding', tokens)
    zero_pad = W2V.Zero_padding(embedding, Batch_size, Maxseq_length, Vector_size)
    result = sess.run(prediction, feed_dict={X: zero_pad, seq_len: [
        len(tokens)]})  # tf.argmax(prediction, 1)이 여러 prediction 값중 max 값 1개만 가져옴
    point = result.ravel().tolist()
    Tag = ["단맛", "신맛", "매운맛", "담백한맛", "감칠맛", "식감", "온", "냉", "가성비", "감성", "활동적인", "조용한", "교훈적인", "데이트"]

    detect_result = list()
    for t, i in zip(Tag, point):

        print(t, round(i * 100, 2), "%")
        if round(i * 100, 2) >= 1.0:
            detect_result.append({

                'label': t,
                'accuracy' : round(i * 100, 2)
            })


    print(detect_result)
    # sess.close()
    return detect_result


def init():

    global W2V, Batch_size, Maxseq_length, Vector_size, prediction, X, seq_len, sess
    print('flag 1')
    W2V = Word2Vec.Word2Vec()
    print('flag 2')
    Batch_size = 1
    Vector_size = 300
    Maxseq_length = 500  # Max length of training data
    learning_rate = 0.001
    lstm_units = 128
    num_class = 14
    keep_prob = 1.0
    print('flag 3')
    X = tf.placeholder(tf.float32, shape=[None, Maxseq_length, Vector_size], name='X')
    Y = tf.placeholder(tf.float32, shape=[None, num_class], name='Y')
    seq_len = tf.placeholder(tf.int32, shape=[None])
    print('flag 4')
    BiLSTM = Bi_LSTM.Bi_LSTM(lstm_units, num_class, keep_prob)
    print('flag 5')
    with tf.variable_scope("loss", reuse=tf.AUTO_REUSE):
        logits = BiLSTM.logits(X, BiLSTM.W, BiLSTM.b, seq_len)
        loss, optimizer = BiLSTM.model_build(logits, Y, learning_rate)
    print('flag 6')
    prediction = tf.nn.softmax(logits)  # softmax
    print('flag 7')
    saver = tf.train.Saver()
    init = tf.global_variables_initializer()
    modelName = "./posting/TextClassifier/Bi_LSTM/Data/Bi_LSTM"
    print('flag 8')
    sess = tf.Session()
    print('flag 9')
    sess.run(init)
    print('flag 10')
    saver.restore(sess, modelName)
    print('flag 11')

    # return W2V, Batch_size, Maxseq_length, Vector_size,prediction, X, seq_len, sess
def text_detect(s):

    # W2V, Batch_size, Maxseq_length, Vector_size, prediction, X, seq_len, sess = init()
    result =Grade(s, W2V, Batch_size, Maxseq_length, Vector_size,prediction, X, seq_len, sess )

    print('results: ', result)
    return result
