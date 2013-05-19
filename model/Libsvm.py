'''
Created on May 18, 2013

@author: jacob
'''
import libsvm.python.svmutil as svmutil

def train( data_file_name, test_file ): 
    y, x = svmutil.svm_read_problem(data_file_name)
    m = len(y)
    model = svmutil.svm_train(y, x, "-c 8 -g 0.3125")

    y1, x1 = svmutil.svm_read_problem( test_file )
    m1 = len(y1)
    p_label, p_acc, p_val = svmutil.svm_predict(y1, x1, model)
    print len(p_label)