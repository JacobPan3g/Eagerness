# coding=utf8
'''
Created on May 20, 2013

@author: jacob
'''

class Book:
    title = "title"
    author = "author"
    isbn10 = "isbn10"
    isbn13 = "isbn13"
    image = "image"
    link = "link"
    #publisher = "publisher"
    #pubdate = "pubdate"
    
    def __init__( self, title="None", author="None", isbn10="None", isbn13="None", image="None", link="None" ):
        self.title = title.encode("utf-8")
        self.author = author.encode("utf-8")
        self.isbn10 = isbn10.encode("utf-8")
        self.isbn13 = isbn13.encode("utf-8")
        self.image = image.encode("utf-8")
        self.link = link.encode("utf-8")
    
    def __str__(self):
        info = "\n".join([self.title, self.author, self.isbn10, self.isbn13, self.image, self.link])
        return "============================================================================\n"+info

# For model testing
if __name__ == '__main__':
    book = Book();
    book.title = "aa"
    print book.title
    print book.author
    print book
    b2=Book()
    print b2
    
    