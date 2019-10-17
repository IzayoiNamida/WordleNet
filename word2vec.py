# -*- coding: utf-8 -*-
 
from gensim.models import word2vec
import logging
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
filename = "nltk.txt"
sentences = word2vec.LineSentence(filename);

model = word2vec.Word2Vec(sentences, size=2,window=25,min_count=2,workers=5,sg=1,hs=1) 

model.save("nltk.model")

model.wv.save_word2vec_format('nltk.model.txt','nltk.vocab.txt',binary=False)

model = word2vec.Word2Vec.load("nltk.model")

sb = model['web'];
print(sb);
