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

papers = [2,3,5,7,8,10,11,13,14,15,16,17,18,19,21,23,25,27,28,32,35,37,44,45,53,60,63,65,67,71,75,81,84,86,94,97,114,118,121,124,125,126];
res = {};
res["path"] = []
fr = open("path.json","w");
for line in open("dataoutcpp.txt"): 
    lines = line.split(" ");
    print(str(papers[int(lines[0])]));
    res["path"].append({
    	"id":str(papers[int(lines[0])]),
    	"path":str(papers[int(lines[1])])+" "+str(papers[int(lines[2])])+" "+str(papers[int(lines[3])]) + " "+str(papers[int(lines[4])])+ " "+str(papers[int(lines[5])])+ " "+str(papers[int(lines[5])])
    	})

fr.write(json.dumps(res,indent=2))  
fr.close();
