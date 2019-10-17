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

filename = "data_1007_relationship.json";
papers = [2,3,5,7,8,10,11,13,14,15,16,17,18,19,21,23,25,27,28,32,35,37,44,45,53,60,63,65,67,71,75,81,84,86,94,97,114,118,121,124,125,126];
f = open(filename);
test = json.load(f);
# print(test["nodes"]);
nodes = test["rlinks"];

res = {};
res["recommendLinks"] = [];
res["nodes"] = [];
ffff = open("dataincpp.txt","w");
for i in range(len(nodes)):
	s1 = nodes[i]["source"];
	s2 = nodes[i]["target"];
	value = nodes[i]["value"];
	print(s1 + " " + s2 + " " + str(value));
	ffff.write(s1 + " " + s2 + " " + str(value) + "\n");
ffff.close();
