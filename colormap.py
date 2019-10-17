import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from gensim import corpora,similarities, models  
from pprint import pprint  
from sklearn import feature_extraction  
from sklearn.feature_extraction.text import TfidfTransformer  
from sklearn.feature_extraction.text import CountVectorizer  
from sklearn.decomposition import PCA  
from sklearn.cluster import SpectralClustering
from openpyxl import load_workbook
from gensim import corpora, models, similarities
from gensim.models import word2vec
import matplotlib.image as mpimg # mpimg 用于读取图片
import matplotlib.pyplot as plt
#--------------------------------------------------------------------
def linear_colormap():
 
    color_map = []
    for i in range(0,256):
        for j in range(0,256):
            color = (i, 120, j);
            color_map.append(color);
    return color_map

#--------------------------------------------------------------------

def draw_colormap(color_map):
    map_image_arr = np.zeros((256, 256, 3), np.uint8)
 
    for i in range(0, 256, 1):
        for j in range(0,256,1):
            map_image_arr[i][j][0] = color_map[i*256 + j][0]
            map_image_arr[i][j][1] = color_map[i*256 + j][1]
            map_image_arr[i][j][2] = color_map[i*256 + j][2]   
            #print(map_image_arr[i][j]);
    map_image = Image.fromarray(map_image_arr)
    map_image.show()
    map_image.save("colormap.png")
    return

def draw_scatter():
    model = word2vec.Word2Vec.load("nltk.model")
    filename = "wordsInWordcloud.txt";
    f1 = open("wordcolor.txt","w");
    f = open(filename).read().split();
    x = [];
    y = [];
    xy = [];
    for i in range(len(f)):
        if(str(f[i]) == "different"):
            continue;
        a = model[str(f[i]).lower()][0] + 2;
        b = model[str(f[i]).lower()][1] + 2;
        x.append(a/1.5 * 255);
        y.append(b/3 * 255);
        r = str(hex(int(a/1.5 *255)));
        g = str(hex(120));
        b = str(hex(int(b/3 * 255)));
        print("#" + r + g + b);
        print("#" + r[2:4] + g[2:4]+ b[2:4]);
        f1.write(str(f[i]) + ": ");
        f1.write("#" + r[2:4] + g[2:4]+ b[2:4])
        f1.write("\n")
        xy.append(model[str(f[i]).lower()]);
    p1 = plt.scatter(x,y,marker = "+");
    plt.show();
    f1.close();
    return;
#--------------------------------------------------------------------

# colormap = linear_colormap();
# draw_colormap(colormap);
draw_scatter();