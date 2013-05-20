'''
FeatureFactor
Created the feature space which contained the feature index and training set

Created on May 20, 2013

@author: jacob
'''
import WordSeg

## ======================================================================================
## some settings
## ======================================================================================
kw_each_label = 100
kw_each_predict = 200
num_of_labels = 2



## ====================================================================================== 
## public method
## ======================================================================================

# Function: getFeature
#     get the train matrix according the feature index
# @param sentence:string        
# @return    f_vector:list
def getFeature( sentence, f_index ):
    kw = WordSeg.getKeyWords( sentence, kw_each_predict )
    f_vector = [0] * kw_each_label * num_of_labels           # all 0 list 
    # get the f_vector for each text
    for i in kw:
        if f_index.has_key( i ):
            f_vector[ f_index[i] ] = 1
    return f_vector

# Function: getAllText
#     get all feature space index and train set 
# @param train_data_dir:string
#        labels:string
#        sample_num:int
# @return    f_index:dict
#            y:list
#            X:matrix
def getFeatureSpace( train_data_dir, labels, sample_num=100 ):
    kws = list()                # list =all key words
    train_set = list()
    for label in labels:
        alltext, texts = getAllText( train_data_dir, label, sample_num )
        kw = WordSeg.getKeyWords(alltext, kw_each_label )
        kws.extend(kw)
        train_set.append( texts );
    #print " ".join(kws)
    #print len(train_set)
    f_index = dict( zip( kws, range( len(kws) ) ) )
    y, X = getTrainMatrix( train_set, f_index )
    return f_index, y, X
    

## ======================================================================================
## private method
## ======================================================================================

# Function: getAllText
#     get all content and summary as a txt for each label
# @param train_data_dir:string
#        label:string
#        sample_num:int
# @return   alltext:string    a string of all text 
#           texts:list        a list contained every text
def getAllText( train_data_dir, label, sample_num=100 ):
    alltext = ""
    texts = list()
    for i in xrange( sample_num ):
        file_name = '%s%s/%d.txt' % ( train_data_dir, label, i )
        #print file_name
        fobj = open(file_name)
        text = fobj.read()
        fobj.close()
        alltext += text;
        texts.append(text);
    #print alltext
    alltext_file_name = '%s%s.txt' % (train_data_dir, label)
    fobj = open( alltext_file_name, 'w' )
    fobj.write(alltext)
    fobj.close()
    return alltext, texts

# Function: getTrainMatrix
#     get the train matrix according the feature index
# @param train_set:list        
#        f_index:dict
# @return    y:list
#            X:matrix
def getTrainMatrix( train_set, f_index ):
    X = list()
    y = list()
    for idx in xrange( len(train_set) ):
    #for group in train_set:
        for text in train_set[idx]:
            f_vector = getFeature(text, f_index)
            X.append( f_vector )
            y.append( idx )
    return y, X
    

# For model testing
if __name__ == '__main__':
    labels = ["it", "economy"]
    f_index, y, X = getFeatureSpace("../train_data_src/", labels, 2)
    print y
    print len(y)
            


            
            
    
    
    