'''
Created on May 20, 2013

@author: jacob
'''
import sys
import jieba.analyse as jieba

def getKeyWords( sentence, num=20 ):
    kw = jieba.extract_tags(sentence, num)
    return kw

# For model testing
if __name__ == '__main__':
    kw = getKeyWords( sys.argv[1] )
    print "/".join( kw )