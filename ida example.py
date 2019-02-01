from __future__ import print_function

from collections import Counter
import json
import os
import codecs

import lda
import matplotlib.pyplot as plt
import numpy as np
import scipy.sparse as sparse
from sklearn.decomposition import LatentDirichletAllocation

import csv

#open_dataset
f = open(os.path.normpath('line3.json'), 'r')

doc_data = json.load(f)
f.close()
all_doc_index = doc_data.keys()
#print('Total Documents: ', len(all_doc_index))


#words_in_document715
#print(','.join(doc_data['715']))

#all_vocabは、重複を許して、全ての単語を格納する
all_vocab = []
for doc_idx in all_doc_index:
    all_vocab += doc_data[doc_idx]

# 重複を消すためにsetしてlistにする
all_vocab = list(set(all_vocab))
vocab_num = len(all_vocab)
#print('Vocablary Number: ', vocab_num)

#学習データとテストデータに分けるため、リストをNumpyの配列にする
all_doc_index_ar = np.array(list(all_doc_index))

#学習データのサンプル数を決める
train_portion = 0.7
train_num = int(len(all_doc_index_ar) * train_portion)

#学習データとテストデータに分ける
np.random.shuffle(all_doc_index_ar)
train_doc_index = all_doc_index_ar[:train_num]
test_doc_index = all_doc_index_ar[train_num:]

#空のスパース行列を定義
A_train = sparse.lil_matrix((len(train_doc_index), len(all_vocab)),
                            dtype=np.int)
A_test = sparse.lil_matrix((len(test_doc_index), len(all_vocab)),
                           dtype=np.int)

#all_vocabのリストの中で、単語のインデックス番号を取得するためNumpy配列にしておく
all_vocab_ar = np.array(all_vocab)
train_doc_index_ar = np.array(train_doc_index)
test_doc_index_ar = np.array(test_doc_index)


# 学習用
train_total_elements_num = 0
for i in range(len(train_doc_index)):
    doc_idx = train_doc_index[i]
    row_data = Counter(doc_data[doc_idx])
    
    for word in row_data.keys():
        word_idx = np.where(all_vocab_ar == word)[0][0]
        A_train[i, word_idx] = row_data[word]
        train_total_elements_num += 1
#print('Train total elements num :', train_total_elements_num)


# テスト用
test_total_elements_num = 0
for i in range(len(test_doc_index)):
    doc_idx = test_doc_index[i]
    row_data = Counter(doc_data[doc_idx])
    
    for word in row_data.keys():
        word_idx = np.where(all_vocab_ar == word)[0][0]
        A_test[i, word_idx] = row_data[word]
        test_total_elements_num += 1
#print('Test total elements num :', test_total_elements_num)

#LDA
n_topics = 20 #topic数
model1 = LatentDirichletAllocation(n_topics, 
                                   doc_topic_prior=0.001,
                                   topic_word_prior=0.5,
                                   max_iter=5,
                                   learning_method='online',
                                   learning_offset=50.,
                                   random_state=0)
model1.fit(A_train)

#トピック×単語
normalize_components = model1.components_ / model1.components_.sum(axis=0)

# http://scikit-learn.org/stable/auto_examples/applications/
# topics_extraction_with_nmf_lda.html　より

#topic表示
n_top_words = 10 #1topicの単語数
for topic_idx, topic in enumerate(normalize_components):
    print('Topic #%d:' % topic_idx)
    print(' '.join([all_vocab_ar[i] for i in
                    topic.argsort()[:-n_top_words - 1:-1]]))
    print()


#topic出現確率
test_doc_topic_data = model1.transform(A_test)
normalize_test_doc_topic_data = \
 test_doc_topic_data / test_doc_topic_data.sum(axis=1, keepdims=True)


#確率表示
for topic_idx, prob in enumerate(normalize_test_doc_topic_data[0]):
    print('Topic #%d: probality: %f' % (topic_idx, prob))


#csv書き出し
'''
a = np.zeros((300,n_topics))
for doc in range(300):
    j = 0
    for topic_idx, prob in enumerate(normalize_test_doc_topic_data[doc]):
        #print('Topic #%d: probality: %f' % (topic_idx, prob))
        a[doc][j] = prob
        j += 1

np.savetxt('lda.csv',a,delimiter=',')
'''
