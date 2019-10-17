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

stop_words = 'stop_words_eng.txt'
stopwords = codecs.open(stop_words,'r').readlines()
stopwords = [ w.strip() for w in stopwords ]
#print(stopwords);
stop_flag = ['x', 'c', 'u','d', 'p', 't', 'uj', 'm', 'f', 'r']
corpus = []
res = {}
res['links'] = []
res['nodes'] = []

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
	f1 = open("word_frequency.txt","w");
	for i in range(1,43,1):
		filename = str(i) + ".txt"
		f = open(filename).read();
		context = tokenization(f.lower());
		for j in range(len(context)):
			f1.write(str(context[j].lower()) + " ");
		f1.write("\n");
		# print(lista);
	return; 
#--------------------------------------------------------------------

read_txt();		