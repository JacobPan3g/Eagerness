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
    
def train( train_data_dir, labels, labels_num ):
    f_index, y, X = FeatureFactor.getFeatureSpace( train_data_dir, labels, labels_num )
    saveTheFSpace( f_index )
    model = Libsvm.train( y, X )
    Libsvm.saveModel( model )

## ======================================================================================
## private method
## ======================================================================================

def saveTheFSpace( f_index ):
    fobj = open( "fSpace.index", 'wb' )
    pickle.dump( f_index, fobj )
    fobj.close()

def loadTheFSpace():
    fobj = open( "fSpace.index", 'rb' )
    f_index = pickle.load( fobj )
    fobj.close()
    return f_index
    
    

# For model testing
if __name__ == '__main__':
    if sys.argv[-1] == 'train': 
        labels = ["it", "economy"]
        train( "../train_data_src/", labels, len(labels) )
    else:
        fobj = open( "../train_data_src/economy/2.txt" )
        text = fobj.read()
        fobj.close()
        print recommend( text )