'''
Created on May 20, 2013

@author: jacob
'''

import Recommendation
import Weibo

## ======================================================================================
## some settings
## ======================================================================================
labels = ["it", "economy"]


## ====================================================================================== 
## public method
## ======================================================================================

def recommend( usr, pwd ):
    allWeibos = Weibo.authentication( usr, pwd )
    label = Recommendation.recommend( allWeibos )
    # douban

def train( train_data_dir, labels, labels_num ):
    Recommendation.train( train_data_dir, labels, labels_num )
    

# For model testing    
if __name__ == '__main__':
    train( "../train_data_src/", labels, len(labels) ) 