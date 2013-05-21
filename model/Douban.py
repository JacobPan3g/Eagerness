# coding=utf8
'''
Created on May 20, 2013

@author: jacob
'''
import random
import urllib
import simplejson
import Book

API_KEY = "0a32af8654e54e6a1e980e92feafeb3e"

def getRecommondBooks( label ):
    # get the recommonded books
    label = urllib.quote(label)
    rand = int(random.uniform( 0, 20 ))
    url = u"http://api.douban.com/book/subjects?alt=json&tag=%s&start-index=%d&max-results=6&apikey=%s" % ( label, rand, API_KEY )
    
    res_json = urllib.urlopen( url ).read()
    res_dict = simplejson.loads( res_json )
    
    books = list()
    for entry in res_dict["entry"]:
        title=entry["title"]["$t"]
        ibsn10=entry["db:attribute"][0]["$t"]
        ibsn13=entry["db:attribute"][1]["$t"]
        image=entry["link"][2]["@href"]
        link=entry["link"][1]["@href"]
        try:
            author=" ".join([ i["name"]["$t"] for i in entry["author"]])
        except:
            author=" "
        book = Book.Book( title,author,ibsn10,ibsn13,image, link )
        books.append(book)

    #for book in books:
    #    print book
    return books

def getTopBooks():
    labels = ["互联网", "文学", "旅游", "经济", "美食" ]
    idx = int(random.uniform( 0, 5 ))
    label = labels[idx]
    books = getRecommondBooks( label )
    return books
    

# For model testing
if __name__ == '__main__':
    label = '互联网'
    label = urllib.quote(label)
    print label
    getRecommondBooks(label)
