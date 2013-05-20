'''
Created on May 18, 2013

@author: jacob
'''
import sys
import libsvm.python.svmutil as svmutil

def train( train_file_name ): 
    y, x = svmutil.svm_read_problem(train_file_name)
    model = svmutil.svm_train(y, x, "-c 8 -g 0.3125")
    return model
    
def predict( test_file_name, model ):
    y1, x1 = svmutil.svm_read_problem( test_file_name )
    p_label, p_acc, p_val = svmutil.svm_predict(y1, x1, model)
    print len(p_label)

# For model testing    
if __name__ == '__main__':
    #print sys.argv[1]
    model = train( sys.argv[1] )
    predict( sys.argv[2], model )