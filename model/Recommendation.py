# coding=utf8
'''
Created on May 20, 2013

@author: jacob
'''
import sys
import FeatureFactor
import Libsvm
import pickle

## ====================================================================================== 
## public method
## ======================================================================================

def recommend( allWeibos ):
    model = Libsvm.loadModel()
    f_index = loadTheFSpace()
    f_vector = FeatureFactor.getFeature( allWeibos, f_index )
    label = Libsvm.predict( f_vector, model )
    return label
    
def train( train_data_dir, labels, sample_num ):
    f_index, y, X = FeatureFactor.getFeatureSpace( train_data_dir, labels, sample_num )
    saveTheFSpace( f_index )
    model = Libsvm.train( y, X )
    Libsvm.saveModel( model )

## ======================================================================================
## private method
## ======================================================================================

def saveTheFSpace( f_index ):
    fobj = open( "data/fSpace.index", 'wb' )
    pickle.dump( f_index, fobj )
    fobj.close()

def loadTheFSpace():
    fobj = open( "data/fSpace.index", 'rb' )
    f_index = pickle.load( fobj )
    fobj.close()
    return f_index
    
    

# For model testing
if __name__ == '__main__':
    if sys.argv[-1] == 'train': 
        #labels = ["it", "economy"]
        #train( "../train_data_src/", labels, 2 )
        labels = [u"互联网", u"文学", u"旅游", u"经济", u"美食" ]
        #labels = ["it", "literature" ]
        train( "../train_data_src/", labels, 90 )
    else:
        fobj = open( u"../train_data_src/经济/91.txt" )
        text = fobj.read()
        fobj.close()
        print recommend( text )