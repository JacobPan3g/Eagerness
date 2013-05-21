# coding=utf8
'''
Created on May 18, 2013

@author: jacob
'''
import sys
import libsvm.python.svmutil as svmutil

## ======================================================================================
## some settings
## ======================================================================================
C = 8
gamma = 0.3125
option = "-c %d -g %lf" % ( C, gamma )


## ====================================================================================== 
## public method
## ======================================================================================

def train( y, X ):
    model = svmutil.svm_train(y, X, option)
    return model

def trainByFile( train_file_name ): 
    y, X = svmutil.svm_read_problem(train_file_name)
    model = train(y, X)
    return model
    
def predict( f_vector, model ):
    X = [ f_vector ]
    y = [ 0 ]
    p_label, p_acc, p_val = svmutil.svm_predict(y, X, model)
    return p_label

def predictByFile( test_file_name, model ):
    y, X = svmutil.svm_read_problem( test_file_name )
    p_label, p_acc, p_val = svmutil.svm_predict(y, X, model)
    print len(p_label)
    
def saveModel( model ):
    svmutil.svm_save_model( 'data/model.file', model )

def loadModel():
    try:
        model = svmutil.svm_load_model( 'data/model.file' )
    except:
        print "Warning: You haven't training for a model. Please call the train() function."
    return model

# For model testing    
if __name__ == '__main__':
    #print sys.argv[1]
    model = trainByFile( sys.argv[1] )
    predictByFile( sys.argv[2], model )