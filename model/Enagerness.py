# coding=utf8
'''
Created on May 20, 2013

@author: jacob
'''

import Recommendation
import Weibo
import Douban

## ======================================================================================
## some settings
## ======================================================================================
labels = ["互联网", "文学", "旅游", "经济", "美食" ]
books = []

## ====================================================================================== 
## public method
## ======================================================================================

def recommend( usr, pwd ):
    userInfo, allWeibos = Weibo.authentication( usr, pwd )
    label = Recommendation.recommend( allWeibos )
    labelIdx = int(label[0])
    tag = labels[labelIdx]
    books = Douban.getRecommondBooks(tag)
    for book in books:
        print book
    return books, userInfo

def train( train_data_dir, labels, labels_num ):
    Recommendation.train( train_data_dir, labels, labels_num )
    
def getTopBooks():
    books = Douban.getTopBooks()
    for book in books:
        print book
    return books

# For model testing    
if __name__ == '__main__':
    #train( "../train_data_src/", labels, len(labels) ) 
    recommend( "zhenjian3g@qq.com", "jacobpan2889184" )
    #getTopBooks()