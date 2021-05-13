# searching part
import json
import os
import sys
import re
import bs4
from bs4 import BeautifulSoup
import json
import numpy as np
import collections
import time
import nltk
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
import pandas as pd
import math
from math import log

def get_words(word = str): 
    ps = PorterStemmer()
    # find out all the words in the path and return a list of words(lowered)
    try:
        l = re.findall('[a-zA-Z]+',word)
        l2 = []
        for i in l:
            keys = ps.stem(i)
            l2.append(keys.lower())
        return l2
    except:
        print("Unexpected error:", sys.exc_info()[0])
        return []
    
def check_correct(l = list):
    # return a list of words appeard in all files and delete stop words in the same time
    stop_words = set(stopwords.words('english'))
    
    file = open('word_files/word_list.json')
    test = json.load(file)
    content = test['1']
    answer = []
    for i in l:
        if i in content:
            if i not in stop_words:
                answer.append(i)
    return answer    


from sklearn.feature_extraction import DictVectorizer
def get_file(target_list = list):
    # return a matrix, including all files and the frequency of the words in the file
    df = len(target_list)
    N = 55393
    data_dict = [{}] * len(target_list)
    for i in range(len(target_list)):
        #print('lets go ?')
        target = target_list[i]
        file_dict = {}
        path = 'word_files/word_files/' + target[0] + '/' + target + '.json'
        file = open(path)
        data_dict_saver = json.load(file)
        for keys in data_dict_saver.keys():
            t = data_dict_saver[keys]
            tf_weight = 1 + log(t[0])
            idf = log(N/df)
            tfidf_weight = tf_weight * idf
            file_dict[keys] = tfidf_weight
        data_dict[i] = file_dict
    return data_dict

# Function to find the column with max Sum 
def colMaxSum(mat): 
    R = len(mat[0])
    C = len(mat)
    idx = -1
    maxSum = -10**9
    for i in range(R): 
        Sum = 0
        for j in range(C): 
            Sum += mat[j][i] 
        if (Sum > maxSum): 
            maxSum = Sum
            idx = i 
    return idx, maxSum 

def get_top_five(data_matrix, dictvectorizer):
    # return the top five file pathes in the data_matrix
    answer = []
    for i in range(5):
        ans, ans0 = colMaxSum(data_matrix)
        #print("Column", ans + 1,"has max Sum", ans0) 
        path_summer = dictvectorizer.get_feature_names()
        #print("File", path_summer[ans],"has max Sum", ans0)
        for i in range(len(data_matrix)):
            data_matrix[i][ans] = 0
        path = path_summer[ans]
        file = open(path)
        data_dict_saver = json.load(file)
        url = data_dict_saver['url']
        answer.append(url)
        
    return answer
               
if __name__ == "__main__":
    searching = input('Searching:')

    t0 = time.time()
    searching = get_words(searching)
    print(searching)
    b = check_correct(searching)
    print(b)
    c = get_file(b)
    #print(c[0])
    data_dict = c
    dictvectorizer = DictVectorizer(sparse=False)
    features = dictvectorizer.fit_transform(data_dict)
    print(len(features[0]))
    print(get_top_five(features,dictvectorizer))

    t1 = time.time()
    print('total running time:')
    print(t1-t0)
