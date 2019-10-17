#coding:utf-8
from numpy import *
import numpy as np
import logging  
import time  
import os  
import jieba  
import glob  
import random  
import copy  
import chardet  
import gensim  
import jieba.analyse 
import jieba.posseg as pseg
import codecs
import json
import re
import nltk
from gensim import corpora,similarities, models  
from pprint import pprint  
from sklearn import feature_extraction  
from sklearn.feature_extraction.text import TfidfTransformer  
from sklearn.feature_extraction.text import CountVectorizer  
from sklearn.decomposition import PCA  
from sklearn.cluster import SpectralClustering
from openpyxl import load_workbook
from gensim import corpora, models, similarities

#--------------------------------------------------------------------

def word2vec(wordlist_1,wordlist_2):
    v1 = []
    v2 = []
    #print(word1,word2);
    #tag_dict1 = {i[0]: i[1] for i in word1}
    #tag_dict2 = {i[0]: i[1] for i in word2}
    # merged_tag = set(word1) | set(word2)
    # for i in merged_tag:
    #     if i in word1:
    #         v1.append(1)
    #     else:
    #         v1.append(0)
    #     if i in word2:
    #         v2.append(1)
    #     else:
    #         v2.append(0)
    # return v1, v2

    word_dict=[]
    for word in wordlist_1:
        # 如果当前词没有加入词汇表，则将该词加入词汇表
        if word not in word_dict:
            word_dict.append(word)
        else:
            continue
    for word in wordlist_2:
        if word not in word_dict:
            word_dict.append(word)
        else:
            continue
    # 3计算词频、4写出词频向量
    word_count_1={}
    word_count_2={}
    word_count_vec_1=[]
    word_count_vec_2=[]
    # 对于词汇表中的每一个词，统计他在每句话中出现的次数
    for word in word_dict:
        num1=wordlist_1.count(word)
        num2=wordlist_2.count(word)
        word_count_1[word]=num1
        word_count_2[word]=num2
        word_count_vec_1.append(num1)
        word_count_vec_2.append(num2)

    # 计算相似度
    vec_1=np.array(word_count_vec_1)
    vec_2=np.array(word_count_vec_2)
    one_dot_two=np.dot(vec_1,vec_2)
    L1=np.sqrt(np.dot(vec_1,vec_1))
    L2=np.sqrt(np.dot(vec_2,vec_2))
    # 余弦值越接近1，就表明夹角越接近0度，也就是两个向量越相似，这就叫"余弦相似性"。
    cos_angle=one_dot_two/(L1*L2)
    #print(cos_angle);
    angle_pi=np.arccos(cos_angle)
    angle=angle_pi*360/2/np.pi
    return cos_angle
    
#--------------------------------------------------------------------

stop_words = 'stop_words_eng.txt'
stopwords = codecs.open(stop_words,'r').readlines()
stopwords = [ w.strip() for w in stopwords ]
#print(stopwords);
stop_flag = ['x', 'c', 'u','d', 'p', 't', 'uj', 'm', 'f', 'r']
corpus = []
res = {}
res['rlinks'] = []
res['nodes'] = []
papers = [2,3,5,7,8,10,11,13,14,15,16,17,18,19,21,23,25,27,28,32,35,37,44,45,53,60,63,65,67,71,75,81,84,86,94,97,114,118,121,124,125,126];
ftxt = "recommend.txt";
fff = open(ftxt,"w");

#--------------------------------------------------------------------

def tokenization(text):
    result = []
    words = pseg.cut(text)
    for word, flag in words:
        if flag not in stop_flag and word not in stopwords:
            result.append(word)
    return result

#--------------------------------------------------------------------

def read_txt():
	fr = open("data_1007_relationship.json","w")
	frrr = open("datacpp.txt","w");
	frr = "data_1006.json";
	fjson = open(frr);
	hasaki = json.load(fjson);
	linkvalue1 = hasaki["links"];
	linkvalue2 = hasaki["force"];
	for i in range(1,43,1):
		filename = str(i) + ".txt"
		f = open(filename).read();
		context = tokenization(f.lower());
		for j in range(1,i,1):
			filename2 = str(j) + ".txt"
			f2 = open(filename2).read();
			print(str(papers[i-1]) + " " +str(papers[j-1]));
			#--------------------------------------------------------------------
			context2 = tokenization(f2.lower());

			paper1 = nltk.FreqDist(context);
			paper2 = nltk.FreqDist(context2);
			#print(str(i) + " and " + str(j) + " : ");
			#context = ["a","b","c","d"];
			#context2 = ["a","c","e"];
			#print(len(list(set(context).intersection(set(context2)))));
			wordDic = {"key":12};
			wordDic.clear();
			for word in list(set(context).intersection(set(context2))):
				ratio = paper1[word] / paper2[word];
				wordDic[word] = ratio;

			newWordDic = sorted(wordDic.items(),key = lambda x:x[1],reverse = True)
			wordlen = len(list(set(context).intersection(set(context2))));
			interFreq = wordlen/15;
			cnt = 0;
			curLine = "";
			curLine2 = "";
			for key in dict(newWordDic):
				cnt = cnt + 1;
				if(cnt/interFreq >= 1):
					curLine = curLine + key + ";";
					curLine2 = curLine + key + " ";
					cnt = 0;
			#print(curLine);
			value1 = word2vec(context,context2);
			value = 0.5 * value1;
			value2 = 0;
			value3 = 0;
			for k in range(len(linkvalue2)):
				if linkvalue2[k]["source"] == str(i) and linkvalue2[k]["target"] == str(j):
					value = value + 0.5 * linkvalue2[k]["value_kw"] + 0.5 * linkvalue2[k]["value_at"];
					value2 = linkvalue2[k]["value_kw"];
					value3 = linkvalue2[k]["value_at"];
			#print(str(papers[i]) + " " + str(papers[j]) + " " + str(value)); 

			res["rlinks"].append({
				"source":str(papers[i-1]),
				"target":str(papers[j-1]),
				"commendword":curLine2,
				"value":value,
				"value_sm":value1,
				"value_kw":value2,
				"value_at":value3
				})
			#--------------------------------------------------------------------
			#print("next");
			#for k in range(0,10,1):
	fr.write(json.dumps(res,indent=2));
	fr.close();


read_txt();
